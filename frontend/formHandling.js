const addButton = document.getElementById('add-button');
const viewButton = document.getElementById('view-button');
const spellDetail = document.getElementById('detail-display');
const spellForm = document.getElementById('add-spell-form');
const editButtonTab = document.getElementById('edit-button-tab')
const submitButton = document.getElementById('submit-but')

addButton.addEventListener('click', function () {
    spellDetail.style.display = 'none';
    spellForm.style.display = 'block';
    spellForm.dataset.mode = 'add';

    addButton.disabled = true;
    viewButton.disabled = false;
    editButtonTab.disabled = false;
    spellForm.reset();
});

viewButton.addEventListener('click', function () {
    spellForm.style.display = 'none';
    spellDetail.style.display = 'block';

    viewButton.disabled = true;
    addButton.disabled = false;
    editButtonTab.disabled = false;
});

editButtonTab.addEventListener('click', function () {
    spellDetail.style.display = 'none';
    spellForm.style.display = 'block';
    spellForm.dataset.mode = 'edit';

    addButton.disabled = false;
    viewButton.disabled = false;
    editButtonTab.disabled = true;



    fetch(`http://localhost:5000/spell/${document.getElementById("spellName").textContent}`)
        .then(response => response.json())
        .then(spell => {
            const spellForm = document.getElementById('add-spell-form');
            spellForm['name'].value = spell.name;
            spellForm['level'].value = spell.level;
            spellForm['school'].value = spell.school;
            spellForm['casting_time_value'].value = spell.casting_time_value;
            spellForm['casting_time_unit'].value = spell.casting_time_unit;
            spellForm['range_value'].value = spell.range_value;
            spellForm['range_unit'].value = spell.range_unit;
            spellForm['component_v'].checked = spell.component_v;
            spellForm['component_s'].checked = spell.component_s;
            spellForm['component_m'].checked = spell.component_m;
            spellForm['material_description'].value = spell.material_description;
            spellForm['description'].value = spell.description;
            spellForm['upcast'].value = spell.upcast;
            spellForm['classes'].value = spell.classes;
            spellForm['source_book'].value = spell.source_book;

        });

});

spellForm.addEventListener('submit', function (event) {
    event.preventDefault();

    let formData = new FormData(spellForm);

    let jsonObject = {};

    for (const [key, value] of formData.entries()) {
        jsonObject[key] = value;
    }

    if (jsonObject.range_value === '') {
        jsonObject.range_value = null;
    }

    if (jsonObject.casting_time_value === '') {
        jsonObject.casting_time_value = null;
    }

    jsonObject.component_v = spellForm['component_v'].checked;
    jsonObject.component_s = spellForm['component_s'].checked;
    jsonObject.component_m = spellForm['component_m'].checked;


    let url, method;
    if (spellForm.dataset.mode === 'add') {
        url = 'http://localhost:5000/spell';
        method = 'POST';
    } else {
        url = `http://localhost:5000/spell/${jsonObject.name}`;
        method = 'PATCH';
    }

    fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonObject)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });

});

document.getElementById('upload-button').addEventListener('click', () => {
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('http://localhost:5000/upload-json', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
});