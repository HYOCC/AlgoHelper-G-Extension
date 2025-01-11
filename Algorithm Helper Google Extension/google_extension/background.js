
chrome.tabs.onActivated.addListener((activeInfo) => {
    chrome.tabs.get(activeInfo.tabId, (tab) => {
        if (tab.url && tab.url.startsWith("http")) {
        // You can perform additional actions with the URL here
            if (tab.url.startsWith("https://leetcode.com/problems/")){
                console.log('Leetcode Question Opened');// Log

                fetch("http://localhost:5000/leetcode", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(tab)
                })
                .then(response => {
                    return response.json();
                })
                .then(data =>{
                    console.log('Recieved from Flask: ', data)
                })

            } else {
                console.log('Not Leetcode');// Log
            }
            

        }
    });
});
  
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (tab.active && changeInfo.url && changeInfo.url.startsWith("http")) {
        console.log("Updated active tab URL:", changeInfo.url);
        // You can perform additional actions with the updated URL here
        if (changeInfo.url.startsWith("https://leetcode.com/problems/") && changeInfo.url.endsWith("description/")){
            console.log('Leetcode Opened');// Log

                fetch("http://localhost:5000/leetcode", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(changeInfo.url)
                })
                .then(response => {
                    return response.json();
                })
                .then(data =>{
                    console.log('Recieved from Flask: ', data)
                })
        } else {
            console.log('Not Leetcode');// Log
        }
    }
});



