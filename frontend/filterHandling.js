const filterForm = document.getElementById('filters');

function getFilters() {
    const sourcebook = document.querySelector('#sourcebook').value;
    const id = document.querySelector('#id').value;
    const spellName = document.querySelector('#spell-name').value;
    const school = document.querySelector('#school').value;
    const level = document.querySelector('#level').value;
    const castingTimeUnit = document.querySelector('#casting-time-unit').value;
    const rangeUnit = document.querySelector('#range-unit').value;
    const classes = Array.from(document.querySelectorAll('input[name="class"]:checked')).map(input => input.id);


    const filters = {
        sourcebook,
        id,
        name: spellName,
        school,
        level,
        casting_time_unit: castingTimeUnit,
        range_unit: rangeUnit,
        classes
    };

    for (let key in filters) {
        if (filters[key] === "") {
            delete filters[key];
        }
    }

    return filters;
}

document.querySelector('#sourcebook').addEventListener('change', function () {
    fetchSpells(getFilters());
});

document.querySelector('#id').addEventListener('input', function () {
    fetchSpells(getFilters());
});

document.querySelector('#spell-name').addEventListener('input', function () {
    fetchSpells(getFilters());
});

document.querySelector('#school').addEventListener('change', function () {
    fetchSpells(getFilters());
});

document.querySelector('#level').addEventListener('change', function () {
    fetchSpells(getFilters());
});

document.querySelector('#casting-time-unit').addEventListener('change', function () {
    fetchSpells(getFilters());
});

document.querySelector('#range-unit').addEventListener('change', function () {
    fetchSpells(getFilters());
});

Array.from(document.querySelectorAll('input[name="class"]')).forEach(checkbox => {
    checkbox.addEventListener('change', function () {
        fetchSpells(getFilters());
    });
});