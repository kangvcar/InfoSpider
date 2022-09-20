window.onload = function () {

  //  console.log(document.getElementsByTagName('pre')[0].innerHTML)
    var data = document.getElementsByTagName('pre')[0].innerHTML;
    chrome.storage.sync.set({'user':data});
    // var content = JSON.stringify(data);
    // var blob = new Blob([data]);
    // saveAs(blob, "users.json");
    chrome.storage.sync.get('flag',function(budget){
        if(budget.flag==1)
        {
            chrome.storage.sync.get('githubname',function(budget){
                var githuburl2="https://api.github.com/users/"+budget.githubname+"/following";
                window.open(githuburl2)
                window.close();

            })
            chrome.storage.sync.set({'flag':0});

        }
    })

}