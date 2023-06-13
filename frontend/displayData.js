function displaySpells(data) {
    const spellsContainer = document.querySelector('.spells');

    spellsContainer.innerHTML = '';

    for (let spell of data) {
        const spellDiv = document.createElement('div');
        spellDiv.className = 'spell';

        const spellName = document.createElement('span');
        spellName.className = 'spell-name';
        spellName.textContent = `${spell.name}`;

        spellName.addEventListener("click", () => getSpellDetails(spell.name));

        const spellLevel = document.createElement('span');
        spellLevel.className = 'spell-level';
        spellLevel.textContent = `| Level ${spell.level} |`;

        const spellSchool = document.createElement('span');
        spellSchool.className = 'spell-school';
        spellSchool.textContent = ` ${spell.school}`;

        spellDiv.appendChild(spellName);
        spellDiv.appendChild(spellLevel);
        spellDiv.appendChild(spellSchool);

        const deleteButton = document.createElement('button');
        deleteButton.className = 'delete-button';
        deleteButton.textContent = 'Delete';

        deleteButton.addEventListener('click', function () {
            fetch(`http://localhost:5000/spell/${spell.name}`, {
                    method: 'DELETE'
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    spellsContainer.removeChild(spellDiv);
                })
                .catch(e => {
                    console.log('There was a problem with the delete request: ' + e.message);
                });
        });

        spellDiv.appendChild(deleteButton);

        spellsContainer.appendChild(spellDiv);
    }

    const resultsCounter = document.getElementById('results');
    resultsCounter.textContent = `${data.length} results`;
}