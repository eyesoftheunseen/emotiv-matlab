function emotiv = emotiv_read()
    global TCP_CONNECTION
    
    emotiv = struct('AF3', [], 'F7', [], 'F3', [], 'FC5', [], 'T7', [], 'P7', [], 'O1', [], ...
                  'O2', [], 'P8', [], 'T8', [], 'FC6', [], 'F4', [], 'F8', [], 'AF4', []);
    
    channel = fieldnames(emotiv);

         
    if (get(TCP_CONNECTION, 'BytesAvailable') > 0)
        receivedString = fscanf(TCP_CONNECTION);
        data = strsplit(receivedString, ',');
        data = str2double(data);
        
        for i = 1:14
            emotiv.(channel{i}) = data(i);
        end
        
    end
end
