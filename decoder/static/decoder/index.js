const narrate_button = document.getElementById("narrate_button");
const btn_div = document.getElementById("play_download_btns");

let sound = new Audio();

const generate_play_button = () => {
	let btn = document.createElement("btn");
	btn.innerHTML = "Play";
	btn.classList.add("btn");
	btn.classList.add("btn-primary");
	btn.classList.add("mt-2");
	btn.onclick = () => {
		sound.play();
	};
	return btn;
};

const generate_download_button = () => {
	let btn = document.createElement("btn");
	btn.classList.add("btn");
	btn.innerHTML = "Download";
	btn.classList.add("btn-primary");
	btn.classList.add("mt-2");
	btn.setAttribute("type", "submit");
	btn.onclick = () => {
		document.getElementById("tts_form").submit();
	};
	return btn;
};

const generate_hidden_input = (text) => {
	let ip = document.createElement("input");
	ip.setAttribute("hidden", true);
	ip.setAttribute("value", text);
	ip.setAttribute("name", "base64_audio");
	return ip;
};

narrate_button.onclick = (event) => {
	let input_text = document.getElementById("input_text");

	if (input_text.value.length === 0) {
		alert("Please enter valid text");
		return;
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
			narrate_button.disabled = false;
			sound = new Audio("data:audio/wav;base64," + data.byte_data.audioContent);

			btn_div.innerHTML = "";

			let download_btn = generate_download_button();
			let play_button = generate_play_button();
			let hidden_ip = generate_hidden_input(data.byte_data.audioContent);

			btn_div.appendChild(download_btn);
			btn_div.appendChild(play_button);
			btn_div.appendChild(hidden_ip);

			narrate_button.innerHTML = "Generate Sound";
		})
		.catch((err) => console.error(err));
};
