function [CIHC, Spast] = initIHCpar( fs, cutoff )
%Function which calculates coeficients for the IHC model Dau
%
%   Input arguments
%         - fs : Sampling frequency
%         - cutoff : cut off frequency of LP filter (1st order Butterworth)
%         
%   Output arguments   
%         - CIHC : Structure which contains filter coef.
%         - Spast : Past values
   
    cutoffNorm = cutoff/(fs/2);
    [b1, a1] = butter(1, cutoffNorm);   % filter coef

    CIHC.b1 = b1;
    CIHC.a1 = a1;
    
    Spast = [];
   
 end

