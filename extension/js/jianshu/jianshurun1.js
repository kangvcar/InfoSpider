window.onload = function () {
    console.log(document.getElementsByTagName('pre')[0].innerHTML)

    data=document.getElementsByTagName('pre')[0].innerHTML;
    chrome.storage.sync.set({'user':data});
    chrome.storage.sync.get('jianshuname',function(budget){

        var jianshuurl2="https://www.jianshu.com/asimov/users/slug/"+budget.jianshuname+"/public_notes";
        window.open(jianshuurl2)
    })
}