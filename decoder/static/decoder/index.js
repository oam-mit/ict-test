const narrate_button = document.getElementById("narrate_button");

narrate_button.onclick = (event) => {

	narrate_button.innerHTML = 'Loading.....';
	event.preventDefault();
	let input_text = document.getElementById('input_text');

    let form_data = new FormData();
    form_data.append('input',input_text.value);

	fetch("/convert_text_to_speech", {
		body: form_data,
        method:"POST"
	})
		.then((data) => data.json())
		.then((data) => {
			narrate_button.innerHTML = 'Narrate';
			var snd = new Audio("data:audio/wav;base64," + data.byte_data.audioContent);
            snd.play();

		})
		.catch((err) => console.error(err));
};
