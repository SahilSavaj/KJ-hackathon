let uploadbtn=document.getElementById('upload-btn');
let filechosen=document.getElementById('file-chosen');
let imagePath=document.getElementById('imageShow');
let clear=document.getElementById('clear');

uploadbtn.addEventListener('change',function(event){
    imagePath.style.display='block';
    imagePath.src=URL.createObjectURL(event.target.files[0]);
    filechosen.textContent=this.files[0].name;
    console.log(imagePath.src);
    imagePath.onload = function() {
        URL.revokeObjectURL(imagePath.src) // free memory
    } 
})



