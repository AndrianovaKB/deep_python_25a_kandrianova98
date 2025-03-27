def search_in_file(file_path, search_words, stop_words):
    search_words = [word.lower() for word in search_words]
    stop_words = [word.lower() for word in stop_words]
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            stop_key = 0
            search_key = 0
            words_in_line = set(line.strip().lower().split())
            for word in stop_words:
                if word in words_in_line:
                    stop_key = 1
                    break
            if stop_key:
                continue
            for word in search_words:
                if word in words_in_line:
                    search_key = 1
                    break
            if search_key:
                yield line.rstrip('\n') 
                    
            
            
                    
            
                    

            

            
