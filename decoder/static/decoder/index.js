const narrate_button = document.getElementById("narrate_button");

narrate_button.onclick = (event) => {
	let input_text = document.getElementById("input_text");
	

	if (input_text.value.length === 0) {
		alert("Please enter valid text");
	}
	narrate_button.innerHTML = "Loading.....";
	narrate_button.disabled = true;
	
	event.preventDefault();

	let form_data = new FormData();
	form_data.append("input", input_text.value);

	fetch("/convert_text_to_speech", {
		body: form_data,
		method: "POST",
	})
		.then((data) => data.json())
		.then((data) => {
			console.log(data.byte_data.audioContent);
			narrate_button.innerHTML = "Narrate";
			narrate_button.disabled = false;
			var snd = new Audio(
				"data:audio/wav;base64," + data.byte_data.audioContent
			);
			snd.play();
		})
		.catch((err) => console.error(err));
};
