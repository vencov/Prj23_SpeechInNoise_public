function [COME, Spast] = initOMEpar( fs )
%Function which calculates coeficients for the filters representing the
%peripheral ear (2 parallels filters - 2 cascade filters)
%
%   Input arguments
%         - fs : Sampling frequency
%         
%   Output arguments   
%         - COME : Structure which contains all parameters for the utilisation of the different filters (peripheral ear)
%         - Spast : Structure used to save the previous values for the calculation of the different filters
   
        
    fc1E1 = 1000; % First Cut-off frequency of filter 1
    fc2E1 = 4000; % Second Cut-off frequency of filter 1       
    fc1E2 = 2500; % First Cut-off frequency of filter 2
    fc2E2 = 7000; % Second Cut-off frequency of filter 2  
    
%% Initialisation of the previous values of filters  

    Spast.S1 = []; % initialisation of the previons data in filter 1
    Spast.S2 = []; % initialisation of the previons data in filter 2
    Spast.S3 = []; % initialisation of the previons data in filter 3
    Spast.S4 = []; % initialisation of the previons data in filter 4
    
%% Parallel filters (External ear)

    [COME.bOE1, COME.aOE1] = butter(1, [fc1E1 fc2E1]/(fs/2)); %  Coefs filter 1
    [COME.bOE2, COME.aOE2] = butter(1, [fc1E2 fc2E2]/(fs/2)); %  Coefs filter 2
    COME.gOE1 = 10.^(10/20); % Gain normalized filter 1
    COME.gOE2 = 10.^(25/20); % Gain normalized filter 2
    
%% Cascade filters (Middle ear)

    dt = 1/fs;
    tau = 1/(2*pi*50);
    a1 = dt/tau-1; 
    a0 = 1;
    b0 = 1+a1;
    
    COME.bME1=b0;  
    COME.aME1=[a0 a1];
    
    [COME.bME2, COME.aME2] = butter(1, 1000/(fs/2), 'high'); % Coefs filter 3  
    COME.gME = 45e-9; % Gain normalized 

 end

