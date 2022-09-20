
window.onload = function () {
    console.log(document.getElementsByTagName('pre')[0].innerHTML)
    let data = document.getElementsByTagName('pre')[0].innerHTML;
    chrome.storage.sync.set({'followers':data});
    // var blob = new Blob([data], {type: "text/plain;charset=utf-8"});
    // saveAs(blob, "followers.json");
    chrome.storage.sync.get('githubname',function(budget){
        var githuburl4="https://api.github.com/users/"+budget.githubname+"/repos";
        window.open(githuburl4)
        window.close();

    })

}