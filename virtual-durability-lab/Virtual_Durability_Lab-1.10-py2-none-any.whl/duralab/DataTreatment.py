# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:23:27 2020

@author: U550787
"""
import sys

if float(sys.version[:3])  >= 3.7 :
    from .TestSample import TestSample
    from .Sample import Sample
else:
    from TestSample import TestSample
    from Sample import Sample
    
import numpy as np
import scipy.stats as s
from scipy.optimize import bisect
import math
from matplotlib import pyplot as plt

class DataTreatment:
    """
        Treatment of test result data
        
        Parameters
        ----------
        confidence : float
            Determinate with one the method available the distribution of the test datas with a certain level of confidance 
        
        name : string
            Define a name to your data treatment (it's use to save an image of the visual model representation)
        
        test_result : Test instance
            Acquire the Test instance 
        
        method : string
            Choose the method used to determinate the distribution estimation
            Choices : 'Johnson_rank', 'Hazard_plotting', 'Maximum_likelihood_estimation', 'Weibays'
        
        save_graph : string (Optional)
            Default : None
            Define the save path of the generated graph.
            
        param_assumption : float (optional)
            Default : μ or β from Sample object
            Define an assumption on the parameter for the Weibull estimation
            
        stress : Sample instance (optional)
            Default : None 
            Used in Stress-strenght method
        
        Raises
        ----------
        ValueError
            Parameter 'test_result' is missing or incorrect. Please enter a Test instance, for further information go to help(Test).
        
        ValueError
            Parameter 'stress' is incorrect. Please enter a Sample instance, for further information go to help(Sample).
        
        ValueError 
            A minimum size of 2 for the sample is required.
        
        ValueError
            Parameter 'method' is missing or incorrect. Please choose one of these : 'Johnson_rank', 'Hazard_plotting', 'Maximum_likekihood_estimation'.
            
        ValueError
            Error. data_type  is incompatible with Johnson_rank method. The data type accepted must be in autorized data_type 
        
        ValueError
            Error. data_type is incompatible with Hazard_plotting method. The data type accepted must be in autorized data_type 
            
        ValueError
            Error. data_type is incompatible with Maximum_likelihood_estimation method. The data type accepted must be in data_type
          
        ValueError
            Error. The B estimation is not between 0.05 and 20
        
        ValueError
            Incorrect Law model estimation.
            
        ValueError 
            Error. data_type is incompatible with Weibayes method. The data type accepted must be in data_type 
        
        
        Methods
        ----------
        johnson_rank(self)
        hazard_plotting(self)
        regresslinear(self)
        mle(self)
        weibayes(self)
        stress_strengh(self)
        model_visualization(self) 
        param_title_graph(self, law_model)
        
        Examples
        ----------
    
    """
    def __init__(self, **kwargs):
        
        self.confidence = kwargs.get("confidence", 0.75)        
        self.test = kwargs.get("test_result", None) 
        
        self.method = kwargs.get("method",None)
        
        self.autorized_method = {"Johnson_rank" : ["Complete Data", "Low Right Censored Data", "Censored Data"], 
                                 "Hazard_plotting" : ["Censored Data"],
                                 "Maximum_likelihood_estimation" : ["Complete Data", "Low Right Censored Data", "Censored Data"],
                                 "Weibayes" : ["Complete Data", "Low Right Censored Data", "Strong Right Censored Data", "Censored Data"]}
        
        #All parameter to build the approximation model will be stocked here
        self.models = {"Normal":{}, "Lognormal":{}, "Weibull":{}, "Exponential":{}}
        #All estimation will be saved in this dict
        self.estimation_result = {"Normal":{}, "Lognormal":{}, "Weibull":{}, "Exponential":{}}
        
        self.name = kwargs.get("name", None)
        self.save_path = kwargs.get("save_path", None)
        
        
        if not self.test or not isinstance(self.test, TestSample):
            raise ValueError("Parameter 'test_result' is missing or incorrect. Please enter a Test instance, for further information go to help(Test).")
        
            
        main_param = {"Exponential": 1/self.test.Sample.scale,
                      "Weibull": self.test.Sample.param1,
                      "Lognormal": self.test.Sample.scale,
                      "Normal": self.test.Sample.loc 
                     }[self.test.Sample.law_text] 
        
        #By default the parameter of the theorical law will be take. β for Weibull, μ for Normal and Lognormal, λ for Exponential
        self.param_assumption = kwargs.get("param_assumption", main_param)
        
        self.stress = kwargs.get("stress", None)
        #Calculate the failure probability with stress-strengh method in PPM
        self.ppm = None
        
        if self.test.Sample.size and self.test.Sample.size == 1 and self.method != "Weibayes":
            raise ValueError("Just Weibayes method available to approximate one sample.")
        elif self.test.Sample.size and self.test.Sample.size < 1 :
            raise ValueError("A minimum size of 2 for the sample is required.")
        
        if not self.stress or not isinstance(self.stress, Sample):
            raise ValueError("Parameter 'stress' is incorrect. Please enter a Sample instance, for further information go to help(Sample).")
            
        self.exec_treatment()
        
    def exec_treatment(self):
        
    
        if self.method == "Johnson_rank":
            
            if self.test.data_type in self.autorized_method[self.method]:
                self.johnson_rank()
            else :
                raise ValueError("Error. %s is incompatible with Johnson_rank method. The data type accepted must be in %s" % (self.test.data_type, str(self.autorized_method[self.method])))
                
        elif self.method == "Hazard_plotting":
            
            if self.test.data_type in self.autorized_method[self.method]:
                self.hazard_plotting()
            else :
                raise ValueError("Error. %s is incompatible with Hazard_plotting method. The data type accepted must be in %s" % (self.test.data_type, str(self.autorized_method[self.method])))
        
        elif self.method == "Maximum_likelihood_estimation":
            
            if self.test.data_type in self.autorized_method[self.method]:
                self.mle()
            else : 
                raise ValueError("Error. %s is incompatible with Maximum_likelihood_estimation method. The data type accepted must be in %s" % (self.test.data_type, str(self.autorized_method[self.method])))
        
        elif self.method == "Weibayes":
            
            if self.test.data_type in self.autorized_method[self.method] and self.test.test != "Failure":
                self.weibayes()
            else : 
                raise ValueError("Error. %s is incompatible with Weibayes method. The data type accepted must be in %s" % (self.test.data_type, str(self.autorized_method[self.method])))
        
        else:
            raise ValueError("Parameter 'method' is missing or incorrect. Please choose one of these : 'Johnson_rank', 'Hazard_plotting', 'Maximum_likekihood_estimation', 'Weibayes'.")
        
        #Graphic representation
        self.model_visualization()
    
    def johnson_rank(self):
        
        if self.test.data_type in ["Complete Data", "Low Right Censored Data", "Censored Data"]:
                
            self.models["Method"] = "johnson_rank"
            
            zi_ri = []
            
            self.test.result.sort(key = lambda x: x[1])
            res = [ round(r[1],0) if r[0] == "NOK" else None for r in self.test.result ]
            components_number  = len(res)
            
            for i, r in enumerate(res):
                if self.test.data_type in ["Complete Data","Low Right Censored Data"]:
                    
                    if r and r not in [ j[0] for j in zi_ri ]:
                        zi_ri.append([r, res.count(r) + zi_ri[len(zi_ri)-1][1] if zi_ri else 1])    
                
                elif self.test.data_type in ["Censored Data"]:
                    
                    if r :
                        zi_ri.append([r, float(components_number + 1. - zi_ri[len(zi_ri)-1][1])/float(components_number + 1. - i) + zi_ri[len(zi_ri)-1][1] if zi_ri else (components_number + 1.)/(components_number + 1. - i) ])
    
            Fi = [ s.beta.ppf(self.confidence, zr[1],components_number-zr[1]+1) for zr in zi_ri]
            
            X = {"Normal" : [ zr[0] for zr in zi_ri ], 
                 "Lognormal" : [ math.log(zr[0]) for zr in zi_ri],
                 "Weibull" : [ math.log(zr[0]) for zr in zi_ri],
                 "Exponential": [ zr[0] for zr in zi_ri ]}
            
            Y = {"Normal" : [ s.norm.ppf(F) for F in Fi],
                 "Lognormal" : [ s.norm.ppf(F) for F in Fi], 
                 "Weibull" : [ math.log(math.log( 1 / (1-F) )) for F in Fi], 
                 "Exponential": [ math.log( 1 / (1-F) ) for F in Fi]}
        
            self.regresslinear(X, Y)
            
                    
    def hazard_plotting(self):
        
        if self.test.data_type in ["Censored Data"]:
            
            self.models["Method"] = "hazard_plotting"
            
            self.test.result.sort(key = lambda x: x[1])
            
            zi = [round(z[1], 2) for z in self.test.result]
            components_number  = len(self.test.result)
            
            Hi = [ sum([ 1./(components_number - i) if r[0] == "NOK" else 0 for i,r in enumerate(self.test.result[:j]) ]) for j in range(1, components_number+1) ]
            zi = [zi[i] for i,H in enumerate(Hi) if H != 0]
            Hi = [H for H in Hi if H !=0 ]
            
            X = {"Normal" : zi,
                 "Lognormal" : [ math.log(z) for z in zi],
                 "Weibull" : [ math.log(z) for z in zi],
                 "Exponential": zi}
            
            Y = {"Normal" : [ s.norm.ppf(1 -math.exp(-H)) for H in Hi],
                 "Lognormal" : [ s.norm.ppf(1 -math.exp(-H)) for H in Hi], 
                 "Weibull" : [ math.log(H) for H in Hi], 
                 "Exponential": Hi}
            
            self.regresslinear(X, Y)
                    
    def regresslinear(self, X, Y):
        
        for m in ["Normal", "Lognormal", "Exponential", "Weibull"]:
                    
            self.models[m]["X"] = X[m]
            self.models[m]["Y"] = Y[m]
                    
            slope, intercept, r_value, p_value, std_err = s.linregress(self.models[m]["X"], self.models[m]["Y"])
            
            self.models[m]["slope"] = slope
            self.models[m]["intercept"] = intercept
            self.models[m]["r_value"] = r_value
            self.models[m]["p_value"] = p_value
            self.models[m]["std_err"] = std_err
            self.estimation_result[m]["r_value"] = r_value
            
            if m == "Normal":
                self.estimation_result[m]["s"] = 1 / self.models[m]["slope"]
                self.estimation_result[m]["m"] = - self.models[m]["intercept"] / self.models[m]["slope"]
                
            elif m == "Lognormal":
                self.estimation_result[m]["sln"] = 1 / self.models[m]["slope"]
                self.estimation_result[m]["mln"] = - self.models[m]["intercept"] / self.models[m]["slope"]
            
            elif m == "Weibull":
                self.estimation_result[m]["b"] = self.models[m]["slope"]
                self.estimation_result[m]["h"] = math.exp(-self.models[m]["intercept"] / self.models[m]["slope"])
                    
            elif m == "Exponential":
                self.estimation_result[m]["l"] = self.models[m]["slope"]
    
    def mle(self):
        """
        Use this method when there are more than 20 test results when data type is right censured data
        """
        
        self.models["Method"] = "mle"
        
        F_50 = []
        F_inf = []
        F_sup = []
        
        components_number = len(self.test.result)
        
        if components_number < 20 and self.test.data_type == "Low Right Censored Data":
            print("The number of test result is too low, a shift between the real values and the find values is possible.")
        
        ti = [round(t[1], 2) for t in self.test.result]
        oi = [1 if r[0]=="NOK" else 0 for r in self.test.result]
    
        #Resolve one degree equation to find beta, the shape parameter
        try :
            b = bisect(lambda x: ( sum( [ t**x * math.log(t) for t in ti ] ) / sum( [ t**x for t in ti ] ) - 1/x ) - sum(  [ o * math.log(ti[i]) for i,o in enumerate(oi) ] ) / sum( oi ), 0.05, 10)
        except:
            raise ValueError("Error. The B estimation is not between 0.05 and 20")
        
        #Beta correct in case the number of sample is under 100
        if components_number < 50 and self.test.data_type in ["Complete Data", "Low Right Censored Data"]:
            b = b * (0.199 * math.log(components_number)**3 - 1.055 * math.log(components_number)**2 + 1.898 * math.log(components_number) - 0.188)
        
        h = (float(sum([ t**b for t in ti ])) / sum( oi ))**(1/b)
        
        matrix = [sum([ oi[i]/(b**2) + ( (t/h)**b ) * math.log(t/h)**2 for i,t in enumerate(ti)]),
                  -sum([ (t/h)**b * (1 + b * math.log(t/h)) - oi[i] for i,t in enumerate(ti)])/h,
                  -sum([ b/(h**2) * (oi[i] - (b + 1) * (t/h)**b ) for i,t in enumerate(ti) ])]
        
        det = 1 / (matrix[0] * matrix[2] - matrix[1]**2 )

        var_b = det * matrix[2]
        var_h = det * matrix[0]
        cov_bh = det * -matrix[1]
        
        norm_sup = s.norm.ppf((1 + self.confidence)/2)
        norm_inf = s.norm.ppf((1 - self.confidence)/2)
        
        #Normal law cumulative distribution interval
        X = np.linspace(s.weibull_min.ppf(0.01, b, scale=h),s.weibull_min.ppf(0.999, b, scale=h), 100)
        
        for x in X:
            u = b * math.log(x/h)
            var_u = (u/b)**2 * var_b + (b/h)**2 * var_h - (2*u/h) * cov_bh
            F_inf.append(1 - math.exp(-math.exp(u + norm_inf * math.sqrt(var_u))))
            F_sup.append(1 - math.exp(-math.exp(u + norm_sup * math.sqrt(var_u))))
            F_50.append(1 - math.exp(-math.exp(u + s.norm.ppf(0.50) * math.sqrt(var_u))))
        
        
        self.estimation_result["Weibull"]["b"] = b
        self.estimation_result["Weibull"]["h"] = h
        self.estimation_result["Weibull"]["b_%.2f"%((1. - self.confidence)/2)] = b * math.exp( norm_inf * math.sqrt(var_b) / b)
        self.estimation_result["Weibull"]["b_%.2f"%((1. + self.confidence)/2)] = b * math.exp( norm_sup * math.sqrt(var_b) / b)
        self.estimation_result["Weibull"]["h_%.2f"%((1. - self.confidence)/2)] = h * math.exp( norm_inf * math.sqrt(var_h) / h)
        self.estimation_result["Weibull"]["h_%.2f"%((1. + self.confidence)/2)] = h * math.exp( norm_sup * math.sqrt(var_h) / h)
        self.estimation_result["Weibull"]["cov_bh"] = cov_bh
        
        for key, r in self.estimation_result["Weibull"].items():
            self.models["Weibull"][key] = r
            
        self.models["Weibull"]["F_0.50"] = F_50
        self.models["Weibull"]["F_%.2f"%((1. - self.confidence)/2)] = F_inf
        self.models["Weibull"]["F_%.2f"%((1. + self.confidence)/2)] = F_sup
        self.models["Weibull"]["X"] = X
        
    def weibayes(self):
        """
        This method is defined by the Bayes theorem. 
        Exponential law is 
        """
        
        size_sample = self.test.Sample.size
        size_failure = len([ 1 for i in self.test.result if i[0] == "NOK"])
        
        if(self.test.Sample.law_text == "Weibull"):
            
            self.models["Method"] = "weibayes"
            
            beta = s.beta.ppf(self.confidence, size_failure + 1, size_sample - size_failure + 1)
            
            self.estimation_result["Weibull"]["b"] = self.param_assumption
            self.estimation_result["Weibull"]["h"] = (self.test.L - self.test.Sample.loc) / ((- math.log(1 - beta)) ** (1 / self.param_assumption))
            
        else :
            raise ValueError("Weibayes can be used just with Weibull law for now.")
            
        
    def stress_strengh(self): 
        """
        Find the failure probability in PPM with stress-strengh method.
        """
        
        self.stress.representation = "Probability_density"
        self.stress.GRAPH = False
        self.stress.exec_sample()
        
        #Stress multiply by strengh
        self.z = self.stress.sample * s.weibull_min.cdf(self.stress.x, c=self.estimation_result["Weibull"]["b"], scale=self.estimation_result["Weibull"]["h"])
        
        self.ppm = np.array([ (self.stress.x[i] - self.stress.x[i-1]) * (self.z[i-1] + self.z[i]) / 2 for i in range(1, len(self.z)) ]).sum() * 1e6
        
    def model_visualization(self):
        
        results = [ key for key, val in self.estimation_result.items() if val != {}]
        len_results = len(results) + 1 if 'Weibull' in results else len(results) 
        
        self.fig, self.ax = plt.subplots(len_results,1)
        
        i = 0
        
        for law_model in results:
        
            ax = self.ax[i] if len_results > 1 else self.ax
                
            
            law = {"Normal" : [ s.norm, {"loc" : self.estimation_result["Normal"]["m"] if "m" in self.estimation_result["Normal"].keys() else None,
                                         "scale" : self.estimation_result["Normal"]["s"]if "s" in self.estimation_result["Normal"].keys() else None}],
                   "Weibull" : [ s.weibull_min,  {"c" : self.estimation_result["Weibull"]["b"] if "b" in self.estimation_result["Weibull"].keys() else None,
                                                  "scale" : self.estimation_result["Weibull"]["h"] if "h" in self.estimation_result["Weibull"].keys() else None}],
                   "Lognormal" : [s.lognorm, {"s" : self.estimation_result["Lognormal"]["sln"]  if "sln" in self.estimation_result["Lognormal"].keys() else None,
                                              "scale" : self.estimation_result["Lognormal"]["mln"]} if "mln" in self.estimation_result["Lognormal"].keys() else None], 
                   "Exponential" : [s.expon, {"scale" : 1/self.estimation_result["Exponential"]["l"]  if "l" in self.estimation_result["Exponential"].keys() else None}] }[law_model]
            
            temp =[None, None]
            temp[0] = law[1].copy()
            temp[1] = law[1].copy()
            temp[0].update({"q": 0.01})
            temp[1].update({"q": 0.99})
            
            x = np.linspace(law[0].ppf(**temp[0]),law[0].ppf(**temp[1]),100)
            
            temp = law[1].copy()
            temp.update({"x": x})
            
            ax.plot(x, law[0].cdf(**temp), 'b-', lw=2, alpha=0.6, label=u"%s cdf estimation %s" % (law_model, self.param_title_graph(law_model))) 
            
            title =  u"%s treatment with %.2f confidence\n" % (self.method, self.confidence) if self.models["Method"] != "johnson_rank" else u"%s treatment with %.2f confidence\nR2 : %.4f" % (self.method, self.confidence, self.estimation_result[law_model]["r_value"]) 
            
            if self.models["Method"] == u"mle":
                temp["c"] = self.estimation_result["Weibull"]["b_%.2f"%((1. - self.confidence)/2)]
                temp["scale"] = self.estimation_result["Weibull"]["h_%.2f"%((1. - self.confidence)/2)]
                ax.plot(x, law[0].cdf(**temp), 'm--', lw=2, alpha=0.6, label=u"cdf %.2f β = %.1f, η = %.2f" % (((1. - self.confidence)/2)*100, self.estimation_result["Weibull"]["b_%.2f"%((1. - self.confidence)/2)], self.estimation_result["Weibull"]["h_%.2f"%((1. - self.confidence)/2)])) 
                
                temp["c"] = self.estimation_result["Weibull"]["b_%.2f"%((1. + self.confidence)/2)]
                temp["scale"] = self.estimation_result["Weibull"]["h_%.2f"%((1. + self.confidence)/2)]
                ax.plot(x, law[0].cdf(**temp), 'c--', lw=2, alpha=0.6, label=u"cdf %.2f β = %.1f, η = %.2f\n" % ( ((1. + self.confidence)/2)*100, self.estimation_result["Weibull"]["b_%.2f"%((1. + self.confidence)/2)], self.estimation_result["Weibull"]["h_%.2f"%((1. + self.confidence)/2)]))  
                
            ax.legend()
            ax.set_title(title)
            ax.set_ylabel("Probability density")
            ax.set_xlabel("Quantifiable life measure")
            
            if law_model == "Weibull":
                i += 1
                self.ax[i].plot(np.log(x), np.log(-np.log(1 - law[0].cdf(**temp))), 'r-', lw=2, alpha=0.6, label="Allan plait weibull representation")
                self.ax[i].set_ylabel("log( -log(1 - F(t)) )")
                self.ax[i].set_xlabel("log(t)")
                self.ax[i].set_yscale('log')
                self.ax[i].set_xscale('log')
                self.ax[i].set_title('Allan Plait representation')
            
            i += 1
        
        
        plt.show()
        #plt.tight_layout()
        
#        if self.save_path:
#            name = "%s/%s.png" % (self.save_path,self.save_name) if self.save_name else "%s/model.png" % self.save_path
#            self.fig.savefig(name.decode('utf-8'), format='png', bbox_inches='tight')
        
        
    def param_title_graph(self, law_model):
    
        if law_model == "Exponential" :
            r = u"\nλ = %.4f" %(self.estimation_result[law_model]["l"])
        elif law_model == "Normal":
            r = u"\nμ = %.2f, σ = %.2f" % (self.estimation_result[law_model]["m"], self.estimation_result[law_model]["s"])
        elif law_model == "Lognormal":
            r = u"\nμ = %.2f, σ = %.2f" % (self.estimation_result[law_model]["mln"], self.estimation_result[law_model]["sln"])
        elif law_model == "Weibull":
            r = u"\nβ = %.2f, η = %.2f" % (self.estimation_result[law_model]["b"], self.estimation_result[law_model]["h"])
        
        return r

class TestDataTreatment:
    """
        Data_treatment Class tests
    
        Parameters
        ----------
        
        Raises
        ----------
 
        Methods
        ----------

    """
    def __init__(self):
        
        from Sample import Sample 
        self.sample = Sample(name="TestPlanEfficiency",size=10, representation="Random_variates", law="Weibull", scale=19000, param1=3)
        self.test =  TestSample(life_objective=20000,sample=self.sample, test_type="Zero_failure")
        
    def functionnal_test(self):
    
        self.treatment = DataTreatment(method="Johnson_rank", test_result=self.test)    
    
    def stress_strengh_test(self):
        """
        Compare result with Excel sheet Exp07 - Docinfo : 00994_18_05960
        """
        self.x = np.linspace(s.norm.ppf(10e-9, loc=5.221 ,scale=0.768), s.norm.ppf(1-10e-9, loc=5.221 ,scale=0.768), 1000)
        
        self.z = (s.norm.pdf(self.x, loc=5.221 ,scale=0.768) * s.weibull_min.cdf(self.x, c=3, loc=0, scale=3940))
        
        self.ppm = np.array([ ((self.x[i] - self.x[i-1]) * (self.z[i-1] + self.z[i])) / 2 for i in range(1, len(self.z))]).sum() * 1e6
        
        print(self.ppm)
        
    def functionnal_test_weibayes(self):
        
        stress_law = Sample(representation="Probability_density",law="Normal", loc=100 ,scale=10) 
        
        self.treatment = DataTreatment(method="Weibayes", test_result=self.test, stress=stress_law)
        self.treatment.stress_strengh()
        print(self.treatment.ppm)
        
        
if __name__ == "__main__": 
    
    test = TestDataTreatment()