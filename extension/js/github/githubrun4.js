
window.onload = function () {
    console.log(document.getElementsByTagName('pre')[0].innerHTML)
    let data = document.getElementsByTagName('pre')[0].innerHTML;
    chrome.storage.sync.set({'repos':data});
    // var blob = new Blob([data], {type: "text/plain;charset=utf-8"});
    // saveAs(blob, "repos.json");
    chrome.storage.sync.get('githubname',function(budget){
        var githuburl5="https://api.github.com/users/"+budget.githubname+"/received_events";
        window.open(githuburl5)
        window.close();
    })

}