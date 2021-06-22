import lalpulsar
from .sft import SFT
import lal
import numpy as np

class LoadSFT:
    

    def __init__(self,sftpath,fmin=None,fmax=None,norm=False,summed=False,filled=False,remove_sft=True,save_rngmed=False,tmin=None,tmax=None,vetolist = None):
        """
        Load an SFT from multiple detectors
        args
        -----------------
        sftpath: str
            path to the sft files, for multiple files separate by semicolon, 'filename1;filename2;.....' can input from multiple detectors
        fmin: float
            minimum frequency to load from sft
        fmax: float
            maximum frequency to load from sft
        norm: bool or int
            normalise sft to running median, if integer running median of that many bins
        summed: bool or int
            sum normalised spectrograms over number of bins (default 48 (1day of 1800s)) or set to value
        filled: bool
            fill the gaps in the sfts with the expected value (2 for normalised sfts, nan for sfts)
        remove_sft: bool
            remove original sft after normalising to running median
        save_rndmed: bool
            save the running median as an estimate of noise floor
        tmin: float
            start time for sfts
        tmax: float
            end time for sfts
        vetolist: list
            list of frequency bins to set to expected value (2 or nan) (and +/- 3 bins of selected bin)
        """
        # load the sft
        self.get_sft(sftpath,fmin=fmin,fmax=fmax,tmin=tmin,tmax=tmax)

        # normalise sft to the running median
        if norm is not None:
            if norm == True:
                # set number of bins to running median to 100 as default
                norm = 100
                self.norm_rngmed(med_width=norm, remove_sft = remove_sft,save_rngmed=save_rngmed)
            elif norm == False:
                pass
            else:
                # set the number of bins for running median
                self.norm_rngmed(med_width=norm, remove_sft = remove_sft,save_rngmed=save_rngmed) 

        # set the frequency bins to veto, i.e. set to mean of spectrogram
        if vetolist is not None:
            self.veto_freq_bins(vetolist)

        # sum sfts over given range
        if summed == False:
            pass
        elif summed:
            if summed == True:
                self.sum_sfts()
            else:
                self.sum_sfts(summed)

        # fill the gaps in the sfts
        if filled:
            # fills gaps with mean of chi2(2) distribution
            self.fill_gaps()
            # fills gaps at start and end of each detector to align sfts
            self.align_sfts()

    def get_sft(self,sftpath,fmin=None,fmax=None,tmin=None,tmax=None,vetolist = None):
        '''
        load an sft to a numpy array, 
        args
        -------
        sftpath : string
            path to the sft file
        detector: string
            which detector i.e 'H1'
        fmin    : float
            minimum frequency
        fmax    : float
            maximum frequency
        tmin    : float
            min time
        tmax    : float
            max time
        '''
        
        # set up contraints for data
        constraints = lalpulsar.SFTConstraints()

        # set fmin and fmax to all sfts as default
        if fmin is None:
            fmin = -1
        if fmax is None:
            fmax = -1

        # only select sfts with start time (epoch) in range tmin-tmax
        if tmin is not None:
            self.tmin_gps = lal.LIGOTimeGPS(int(tmin),0)
            constraints.minStartTime=self.tmin_gps
        if tmax is not None:
            self.tmax_gps = lal.LIGOTimeGPS(int(tmax),0)
            constraints.maxStartTime=self.tmax_gps

        # create cataologue of sfts under specified constraints
        catalogue = lalpulsar.SFTdataFind(sftpath,constraints)

        # load the sfts from the catalogue above (currently uses multi SFTs as there is a memory leak in LoadSFTs)
        # sfts = lalpulsar.LoadSFTs(catalogue,fmin,fmax)
        sfts = lalpulsar.LoadMultiSFTs(catalogue,fmin,fmax)
        # keep sft set
        #self.sfts_old = sfts

        # define length of sfts in sft index and number of frequency bins
        # N = sfts.length
        self.det_names = []
        tsft = []
        nbins = []
        for det in sfts.data:
            tsft.append(1.0/det.data[0].deltaF)
            nbins.append(det.data[0].data.length)
        
        if len(set(tsft)) > 1:
            print("Warning: tsft not the same between detectors.")
            
        if len(set(nbins)) > 1:
            print("Warning: different detectors do not have the same number of frequency bins")
        
        for det in sfts.data:
            # get detectors name
            detname = det.data[0].name
            self.det_names.append(detname)

            # initialise SFT for detector
            data = SFT()

            # set parameters of sft
            data.nsft = det.length
            data.nbins = det.data[0].data.length
            data.delta_f = det.data[0].deltaF
            data.f0 = det.data[0].f0
            data.tsft = 1.0/det.data[0].deltaF

            #define range of frequency bin centers
            data.frequencies = np.arange(data.nbins)*data.delta_f + data.f0
            
            # create empty arrays for likleyhoods and epochs
            data.sft = np.zeros((data.nsft,data.nbins)).astype(np.complex_)
            data.epochs = np.zeros(data.nsft)
            # set fmin and fmax
            data.fmin = det.data[0].f0
            data.fmax = data.fmin + data.nbins/data.tsft

            #for i,sft in enumerate(sfts.data):
            for i,sft in enumerate(det.data):
                # fill sft with data
                data.sft[i,:] = sft.data.data
                # record epoch of each sft
                data.epochs[i] = sft.epoch
                
            # save sft for detector
            setattr(self,detname,data)

            
   
    def norm_rngmed(self,med_width=100,remove_sft = False, save_rngmed=False):
        """
        normalise the SFT to the running median and save the output power
        args
        ---------------
        med_width: int (optional)
            number of bins to use for running median, default 100
        remove_sft: bool
            remove the original complex sfts save only the normalised power, default false
        save_rngmed: bool
            save the running median to use as noise floor later, default false
        """

        for det in self.det_names:
            # get sft for detector
            sfts = getattr(self,det)
            
            # create empty vectors for sft and normalised power
            sig2 = lal.CreateREAL8FrequencySeries(None,0,0,1./sfts.tsft,lal.SecondUnit,sfts.nbins)
            c_sft = lal.CreateCOMPLEX8FrequencySeries(None,0,0,1./sfts.tsft,lal.SecondUnit,sfts.nbins)
            sfts.norm_sft_power = np.zeros((sfts.nsft,sfts.nbins))

            if save_rngmed:
                sfts.rng_med = np.zeros((sfts.nsft,sfts.nbins))

            for i,sft in enumerate(sfts.sft):
                # fill sig2 structure with running medians 
                c_sft.data.data = sft.astype('complex64')
                lalpulsar.SFTtoRngmed(sig2,c_sft,med_width)
                if save_rngmed:
                    sfts.rng_med[i,:] = sig2.data.data
                # fill likleyhood arrays with sft data normalised to running median (multiplied by two to be chi2 distribution)
                sfts.norm_sft_power[i,:] = 2*np.abs(c_sft.data.data/np.sqrt(sig2.data.data))**2

            if remove_sft:
                del sfts.sft
                
                
    def veto_freq_bins(self,vetolist):
        """
        If frequency bins to be vetoed, set to mean of nornalised chi2 for spectrogram power or nans for sfts
        Vetoes the input bin and +/- 2 bins 
        args
        -----------
        vetolist: list
            list of frequency bins to be vetoes
        """
        for det in self.det_names:
            sft = getattr(self,det)

            if vetolist is not None:
                if len(np.shape(vetolist)) == 0:
                    vetolist = [vetolist]
                for k in list(vetolist):
                    j = int(np.round((k-sft.fmin)*sft.tsft))
                    # set surrounding bins to veto
                    for i in [j-2,j-1,j,j+1,j+2]:
                        try:
                            if hasattr(sft,"sft"):
                                sft.sft[:,i] = np.ones(sft.nsft)*np.nan
                            if hasattr(sft,"norm_sft_power"):
                                sft.norm_sft_power[:,i] = np.ones(sft.nsft)*2
                            if hasattr(sft,"summed_norm_sft_power"):
                                sft.summed_norm_sft_power[:,i] = np.ones(sft.nsft)*96
                        except IndexError: 
                            pass

            
    def fill_gaps(self):
        '''
        fill data gaps with twos, it is filled with twos as it should have a mean of two, this becomes useful when summing over a day.
        args
        ------
        epochs     : array
            start times of current sfts
        likleihootd : array
            sft likelihood arrays
        tsft       : float
            length of sfts
        returns
        ---------
        new_index : new likleyhood array with time gaps filled with twos
        sft_index : index of each sft
        new_epoch : epochs after data is filled
        '''
        

        for det in self.det_names:
            sft = getattr(self,det)
            # set epochs index for each sft
            sft_index = np.floor((sft.epochs - sft.epochs[0])/sft.tsft).astype('int')

            if hasattr(sft,"sft"):
                if sft.sft is not None:
                    # set equally spaced epochs from start time to end time
                    new_sft = np.array(np.ones((sft_index[-1]+1,sft.sft.shape[1]))*2).astype("complex")
                    # fill appropriate epochs with real data
                    for i,idx in enumerate(sft_index):
                        new_sft[idx,:] = sft.sft[i,:]
                    sft.sft = new_sft
                    del new_sft

            if hasattr(sft,"norm_sft_power"):
                if sft.norm_sft_power is not None:
                    new_sft = np.ones((sft_index[-1]+1,sft.norm_sft_power.shape[1]))*2
                    for i,idx in enumerate(sft_index):
                        new_sft[idx,:] = sft.norm_sft_power[i,:]
                    sft.norm_sft_power = new_sft

            if hasattr(sft,"rng_med"):
                if sft.rng_med is not None:
                    new_sft = np.ones((sft_index[-1]+1,sft.rng_med.shape[1]))*np.nan
                    for i,idx in enumerate(sft_index):
                        new_sft[idx,:] = sft.rng_med[i,:]
                    sft.rng_med = new_sft

            # rerun summing of sfts
            if hasattr(sft,"summed_norm_sft_power"):
                sft.sum_sft()

            # define new epochs for filled data
            new_epoch = np.arange(len(new_sft))*sft.tsft + sft.epochs[0]
            sft.epochs = new_epoch
            sft.nsft = len(sft.epochs)


    def align_sfts(self):
        """
        fill the start and end portions of sfts such that each detector has the same length of data
        """
        # define minimim and maximum epochs
        min_ep = np.inf
        max_ep = -np.inf
        min_det = None
        max_det = None
        tsft = None
        for det in self.det_names:
            det_data = getattr(self,det)
            tsft = det_data.tsft
            min_ep_temp = min(det_data.epochs)
            max_ep_temp = max(det_data.epochs)
            if min_ep_temp < min_ep:
                min_ep = min_ep_temp
                min_det = det
            if max_ep_temp > max_ep:
                max_ep = max_ep_temp
                max_det = det

        # define total number of epochs from minmax and tsft
        num_ep = np.floor((max_ep - min_ep)/tsft).astype("int")

        for det in self.det_names:
            sft = getattr(self,det)
            # find epoch indicies
            sft_index = np.floor((sft.epochs - min_ep)/sft.tsft).astype('int')

            if hasattr(sft,"sft"):
                new_sft = np.array(np.ones((num_ep+1,sft.sft.shape[1]))*2).astype("complex")
                for i,idx in enumerate(sft_index):
                    new_sft[idx,:] = sft.sft[i,:]
                sft.sft = new_sft
                del new_sft

            if hasattr(sft,"norm_sft_power"):
                new_sft = np.ones((num_ep+1,sft.norm_sft_power.shape[1]))*2
                for i,idx in enumerate(sft_index):
                    new_sft[idx,:] = sft.norm_sft_power[i,:]
                sft.norm_sft_power = new_sft

            if hasattr(sft,"rng_med"):
                new_rng = np.ones((num_ep+1,sft.rng_med.shape[1]))*2
                for i,idx in enumerate(sft_index):
                    new_rng[idx,:] = sft.rng_med[i,:]
                sft.rng_med = new_rng


            new_epoch = np.arange(len(new_sft))*sft.tsft + sft.epochs[0]
            sft.epochs = new_epoch
            sft.nsft = len(sft.epochs)

            if hasattr(sft,"summed_norm_sft_power"):
                sft.sum_sft()

        
            
    def sum_sfts(self,sum_type="norm_sft_power",gap_val = 2,nsfts=48):
        '''
        takes input sfts with tsft=1800s and returns sum of 48 sfts, i.e summing over a day
        and returns fraction of real data in each sum.
        args
        -------
        gap_val: double
            value used when there are gaps in the data (for calculating fraction)
        returns
        -----------
        data_av: array
            data summed over every day
        fraction: array
            fraction of each day which contained real data
        '''
        for dt in self.det_names:
            data = getattr(self,dt)
            data.sum_sft(sum_type=sum_type,gap_val=gap_val,nsfts=nsfts,remove_original=False)

    def downsamp_frequency(self,data_type="summed_norm_sft_power",stride = 2,remove_original=False):
        '''
        downsample frequency of sfts by taking mean of a number (stride) of frequency bins starting from base of band
        args
        -------
        stride: int
            number of frequency bins to take mean of and downsample by
        '''
        for dt in self.det_names:
            data = getattr(self,dt)
            data.downsamp_frequency(data_type=data_type,stride=stride,remove_original=remove_original)

