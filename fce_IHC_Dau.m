function [ sigOutIHC, SpastOut] = fce_IHC_Dau(xIn, CIHC, Spast)
%Function which simulates the IHC function (half-wave rectification and low-pass filterin)
%   input arguments   
%        - in : Signal to process
%        - CIHC : Structure which contains filter coef.
%        - Spast : Past values for buffer processing
% 
%   Output arguments 
%        - SigOutIHC : Output matrix
%        - Spast : Past values for calculation of future values of filters


xIn(xIn < 0) = 0; % half-wave rectification

% signal is then filtered by a LP filter
sigOutIHC = zeros(size(xIn));

Nch = size(xIn,2);

if isempty(Spast)

    for k = 1:Nch
        [sigOutIHC(:,k), SpastOut(:,k)] = filter(CIHC.b1,CIHC.a1,xIn(:,k));
    end
else
    
    for k = 1:Nch
        [sigOutIHC(:,k), SpastOut(:,k)] = filter(CIHC.b1,CIHC.a1,xIn(:,k),Spast(:,k));
    
    end
end

