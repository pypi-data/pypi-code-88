from math import isnan

from occamypy import Solver, Problem, Operator
from occamypy.utils import ZERO


class CNN(Operator):
    def __init__(self, domain, range, architecture, name: str = None):
        super(CNN, self).__init__(domain, range)
        self.architecture = architecture
        self.name = name
    
    def forward(self, add, model, data):
        self.checkDomainRange(model, data)
        if not add:
            data.zero()
        data[:] += self.architecture(model.getNdArray())
        
    def __str__(self):
        if self.name is not None:
            return str(self.name[:8])
        else:
            return "  CNN  "
        
    @property
    def parameters(self):
        return self.architecture.parameters()
    

class DeepPriorProblem(Problem):
    def __init__(self, problem: Problem, cnn: CNN):
        """
        Cast a problem to Deep Prior paradigm

        .. math ::
            1 / 2 |A m - d|_2^2
        
        will become:
        
        .. math ::
            1 / 2 |A f(z) - d|_2^2
    
        having
        
        .. math ::
            m = f(z)
            
        where f() is the CNN, and z is a input noise tensor.
        """
        super(DeepPriorProblem, self).__init__()
    
        # necessary attributes
        self.problem = problem
        self.cnn = cnn
        self.op = problem.op
        self.model = self.cnn.domain
        self.output = self.cnn.range
        self.data = self.problem.data
        self.res = self.data.clone().zero()
        
        # other stuff
        self.dres = None
        self.grad = self.problem.grad
        self.setDefaults()
        self.linear = False
        return
    
    def objf(self, residual):
        """Method to return objective function value 1/2 | A f(z) - d |_2"""
        obj = self.problem.obj(residual)
        return obj
    
    def resf(self, model):
        """Method to return residual vector r = A f(z) - d"""
        # computing m = f(z)
        self.cnn.forward(False, model, self.output)
        # Computing A m
        if self.output.norm() != 0.:
            self.op.forward(False, self.output, self.res)
        else:
            self.res.zero()
        # Computing A m - d
        self.res.scaleAdd(self.data, 1., -1.)
        return self.res

    def gradf(self, model, res):
        """Method to return gradient vector g = A'r = A'(A f(z) - d)"""
        self.op.adjoint(False, self.grad, res)
        # TODO add autograd on cnn?
    
    
class DeepPriorSolver(Solver):
    """Deep Prior solver for Re problems"""
    
    # Default class methods/functions
    def __init__(self, optimizer, stopper, logger=None, mod_tol: float = 1e-10):
        """
        Constructor for Deep Prior Solver:
        :param optimizer: torch.opt optimizer
        :param stopper: Stopper, object to terminate inversion
        :param logger: Logger, object to write inversion log file [None]
        :param mod_tol: stop criterion for relative change of model norm
        """
        # Calling parent construction
        super(DeepPriorSolver, self).__init__()
        # Defining stopper object
        self.stopper = stopper
        # define a torch optimizer
        self.optimizer = optimizer
        # Logger object to write on log file
        self.logger = logger
        # Overwriting logger of the Stopper object
        self.stopper.logger = self.logger
        # print formatting
        self.iter_msg = "iter = %s, obj = %.5e, resnorm = %.2e"
        
        self.mod_tol = mod_tol
        
    def __del__(self):
        """Default destructor"""
        return
    
    def run(self, problem: DeepPriorProblem, verbose=False, restart=False):
        """Running Deep Prior solver"""
        self.create_msg = verbose or self.logger

        # overriding save_grad variable
        self.save_grad = False

        # Resetting stopper before running the inversion
        self.stopper.reset()
        
        # initialize all the vectors
        dp_mdl = problem.model.clone()
        dp_out = problem.output.clone()
        dp_out_old = dp_out.clone()

        if restart:
            self.restart.read_restart()
            iiter = self.restart.retrieve_parameter("iter")
            initial_obj_value = self.restart.retrieve_parameter("obj_initial")
            dp_mdl = self.restart.retrieve_vector("dp_mdl")
            dp_out = self.restart.retrieve_vector("dp_out")
            if self.create_msg:
                msg = "Restarting previous solver run from: %s" % self.restart.restart_folder
                if verbose:
                    print(msg)
                if self.logger:
                    self.logger.addToLog(msg)
        else:
            iiter = 0
            if self.create_msg:
                msg = 90 * '#' + '\n'
                msg += "\t\t\tDEEP PRIOR INVERSION log file\n\n"
                msg += "\tRestart folder: %s\n" % self.restart.restart_folder
                msg += "\tModeling Operator:\t%s\n" % problem.op
                msg += "\tDeep Prior CNN   :\t%s\n" % problem.cnn
                msg += 90 * '#' + '\n'
                if verbose:
                    print(msg.replace(" log file", ""))
                if self.logger:
                    self.logger.addToLog(msg)
        
        # main iteration loop
        while True:
            obj0 = problem.get_obj(dp_mdl)
            dp_out_old.copy(dp_out)
            
            if iiter == 0:
                initial_obj_value = obj0
                self.restart.save_parameter("obj_initial", initial_obj_value)
                if self.create_msg:
                    msg = self.iter_msg % (str(iiter).zfill(self.stopper.zfill),
                                           obj0,
                                           problem.get_rnorm(dp_mdl))
                    if verbose:
                        print(msg)
                    if self.logger:
                        self.logger.addToLog("\n" + msg)
        
            if isnan(obj0):
                raise ValueError("Objective function values NaN!")
            
            if obj0 <= ZERO:
                print("Objective function is numerically zero! Stop the inversion")
                break

            self.save_results(iiter, problem, force_save=False)
            
            # check objective function
            obj1 = problem.get_obj(dp_mdl)
            # optimize CNN
            obj1.backward()
            self.optimizer.step(obj1)
            
            # check output update tolerance criterion
            dp_out_norm = dp_out.norm()
            chng_norm = dp_out_old.scaleAdd(dp_out, 1., -1.).norm()
            if chng_norm <= self.mod_tol * dp_out_norm:
                if self.create_msg:
                    msg = "Relative output change (%.4e) norm smaller than given tolerance (%.4e)" \
                          % (chng_norm, self.mod_tol * dp_out_norm)
                    if verbose:
                        print(msg)
                    if self.logger:
                        self.logger.addToLog(msg)
                break
            
            iiter += 1
            if self.create_msg:
                msg = self.iter_msg % (str(iiter).zfill(self.stopper.zfill),
                                       obj0,
                                       problem.get_rnorm(dp_mdl))
                if verbose:
                    print(msg)
                if self.logger:
                    self.logger.addToLog("\n" + msg)

            # saving in case of restart
            self.restart.save_parameter("iter", iiter)
            self.restart.save_vector("dp_out", dp_out)

            if self.stopper.run(problem, iiter, initial_obj_value, verbose):
                break

        # writing last inverted model
        self.save_results(iiter, problem, force_save=True, force_write=True)

        # ending message and log file
        if self.create_msg:
            msg = 90 * '#' + '\n'
            msg += "\t\t\tDEEP PRIOR INVERSION log file end\n"
            msg += 90 * '#'
            if verbose:
                print(msg.replace(" log file", ""))
            if self.logger:
                self.logger.addToLog("\n" + msg)

        # Clear restart object
        self.restart.clear_restart()


if __name__ == "__main__":
    import occamypy
    import numpy as np
    import segmentation_models_pytorch as smp
    import torch
    
    # reference image
    x = np.load("./tutorials/data/monarch.npy").astype(float)
    x = occamypy.VectorTorch(x[None, None]).scale(1 / 255)
    
    # noisy image
    y = x.clone() + x.clone().randn(40.)
    
    # input tensor
    z = occamypy.VectorTorch((1, 64, *x.shape[2:])).randn()
    
    # deep prior cnn
    f = CNN(domain=z, range=x, name="unet_R18",
            architecture=smp.Unet(in_channels=z.shape[1],
                                  classes=x.shape[1],
                                  encoder_name="resnet18",
                                  encoder_weights=None,
                                  activation=None))
    
    x_hat = f*z

    # linear problem: 1/2 |Ax - y|_2^2
    lin_problem = occamypy.LeastSquares(x.clone(), y, occamypy.Identity(x))
    # deep prior formulation: x = f(z)
    dip_problem = DeepPriorProblem(lin_problem, cnn=f)
    
    DIP = DeepPriorSolver(
        optimizer=torch.optim.Adam(f.parameters, lr=0.001),
        stopper=occamypy.BasicStopper(1000),
        logger=None,
    )
    
    DIP.run(dip_problem, verbose=True)
