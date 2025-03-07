function offSwitch() {
    document.getElementById("image").src="https://th.bing.com/th/id/OIP.XFDSAS0ZQmfXoLuCfGH0rQHaEK?rs=1&pid=ImgDetMain";  
    document.getElementById("switchmode").textContent="Switch Off";
    document.getElementById("offmode").style.backgroundColor="red";
    document.getElementById("onmode").style.backgroundColor="white"; 


    
} 
function onSwitch()  {
    document.getElementById("image").src="https://live.staticflickr.com/3849/14774443480_6de16292bf_b.jpg";
    document.getElementById("switchmode").textContent="Switch On";
    document.getElementById("onmode").style.backgroundColor="green";
    document.getElementById("offmode").style.backgroundColor="white";
}