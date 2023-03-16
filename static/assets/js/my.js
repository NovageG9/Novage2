// document.getElementById('mapp').contentDocument.addEventListener('click', () => {
// 	window.location.href = "service.html"
// })

function addcomme(){
		var value= document.getElementById("com");
		var p= document.createElement("p");
		p.innerHTML='<hr>'+value.value;
		document.getElementById("comArea").prepend(p); 
		value.value=null;
}
let num = 0 
function like(){
	let a = document.getElementById('like')
	num += 1;
	a.innerText = num + " likes";
}

function addFavo(){
	alert("Il est bien ajouté dans votre list de favorable.")
}
