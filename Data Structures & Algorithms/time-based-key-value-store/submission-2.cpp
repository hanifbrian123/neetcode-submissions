class TimeMap {
public:
    unordered_map<string, vector<int>> keyHAStimestamps;
    unordered_map<string, unordered_map<int, string>> keyHAStsHASval;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        this->keyHAStsHASval[key][timestamp] = value;
        this->keyHAStimestamps[key].push_back(timestamp);
    }
    
    string get(string key, int timestamp) {
        vector<int> & ts = this->keyHAStimestamps[key];
        int l = -1, r = ts.size()-1;
        while (l < r)
        {
            int mid = (l+r+1)/2;
            if (ts[mid] <= timestamp)
                l = mid;
            else
                r = mid - 1;
        }
        if (l==-1)
            return "";
        else 
            return this->keyHAStsHASval[key][ts[l]];
    }
};