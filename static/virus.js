var selectedOption = 0;
var selectedFiles = []
var formData = new FormData();


function handleOption(myRadio) {
    selectedOption = myRadio.value;
}

function showFileNames(input) {
    const fileList = input.files;
    const output = document.getElementById('file-names');
    
    if (fileList.length === 0) {
        output.innerHTML = "No file selected";
    } else {
        let names = [];
        for (let i = 0; i < fileList.length; i++) {
            names.push(fileList[i].name);
            formData.append('file',fileList[i])
        }
        output.innerHTML = names.join('<br>');
    }
}
function handleConfirm(){
    formData.append('option',selectedOption)

    fetch('/handleFilesSubmission', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.results)
      
    });
}

