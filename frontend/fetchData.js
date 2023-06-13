function fetchSpells(filters) {
    let url = 'http://localhost:5000/spells';

    if (filters) {
        url += '?' + new URLSearchParams(filters);
    }

    fetch(url)
        .then(response => response.json())
        .then(displaySpells);
}

function getSpellDetails(name) {
    fetch(`http://localhost:5000/spell/${name}`)
        .then((response) => response.json())
        .then((spell) => {
            const classesList = document.getElementById("classesList");
            while (classesList.firstChild) {
                classesList.removeChild(classesList.firstChild);
            }
            document.getElementById("spellName").textContent = spell.name;
            document.getElementById("spellLevel").textContent = spell.level;
            document.getElementById("spellSchool").textContent = spell.school;
            document.getElementById("castingTimeValue").textContent = spell
                .casting_time_value;
            document.getElementById("castingTimeUnit").textContent = spell
                .casting_time_unit;
            document.getElementById("rangeValue").textContent = spell.range_value;
            document.getElementById("rangeUnit").textContent = spell.range_unit;
            document.getElementById("components").textContent = getComponents(spell);
            document.getElementById("materialDescription").textContent = spell.component_m && spell.component_m.trim() !== '' ? spell.material_description : "None";

            document.getElementById("sourceBook").textContent = spell.source_book;
            document.getElementById("description").textContent = spell.description;
            document.getElementById("upcast").textContent = spell.upcast;

            function getComponents(spell) {
                let components = "";
                if (spell.component_v) components += "V ";
                if (spell.component_s) components += "S ";
                if (spell.component_m) components += "M";
                return components.trim();
            }

            if (spell.classes) {
                spell.classes.split(",").forEach((className) => {
                    const listItem = document.createElement("li");
                    listItem.textContent = className.trim();
                    classesList.appendChild(listItem);
                });
            }
        });
}

window.onload = function () {
    fetch('http://localhost:5000/sourcebooks')
        .then(response => response.json())
        .then(data => {
            const sourcebookDropdown = document.querySelector('#sourcebook');

            for (let sourcebook of data) {
                const option = document.createElement('option');
                option.value = sourcebook;
                option.text = sourcebook;
                sourcebookDropdown.add(option);
            }
        });

    fetchSpells();
}