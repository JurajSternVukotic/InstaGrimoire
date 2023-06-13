fetch('http://localhost:5000/spells')
    .then(response => response.json())
    .then(spells => {
        let spellCountsByLevel = {};
        for (let spell of spells) {
            let level = spell.level;
            if (!(level in spellCountsByLevel)) {
                spellCountsByLevel[level] = 0;
            }
            spellCountsByLevel[level]++;
        }

        let labels = Object.keys(spellCountsByLevel);
        let data = Object.values(spellCountsByLevel);

        let ctx = document.getElementById('spells-by-level').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Number of spells by level',
                    data: data,
                    backgroundColor: 'rgba(140, 192, 192, 1)',
                    borderColor: 'rgba(240, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });

fetch('http://localhost:5000/spells')
    .then(response => response.json())
    .then(spells => {
        let spellCountsBySchool = {};
        for (let spell of spells) {
            let school = spell.school;
            if (!(school in spellCountsBySchool)) {
                spellCountsBySchool[school] = 0;
            }
            spellCountsBySchool[school]++;
        }

        let labels = Object.keys(spellCountsBySchool);
        let shortLabels = labels.map(label => label.substring(0, 3));
        let data = Object.values(spellCountsBySchool);

        let ctx = document.getElementById('spells-by-school').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: shortLabels,
                datasets: [{
                    label: 'Number of spells by school',
                    data: data,
                    backgroundColor: 'rgba(140, 192, 192, 1)',
                    borderColor: 'rgba(240, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });

fetch('http://localhost:5000/spells')
    .then(response => response.json())
    .then(spells => {
        let spellCountsBySourcebook = {};
        for (let spell of spells) {
            let sourcebook = spell.source_book;
            if (!(sourcebook in spellCountsBySourcebook)) {
                spellCountsBySourcebook[sourcebook] = 0;
            }
            spellCountsBySourcebook[sourcebook]++;
        }

        let labels = Object.keys(spellCountsBySourcebook);
        let data = Object.values(spellCountsBySourcebook);

        let ctx = document.getElementById('spells-by-sourcebook').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Number of spells by sourcebook',
                    data: data,
                    backgroundColor: 'rgba(140, 192, 192, 1)',
                    borderColor: 'rgba(240, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    x: {
                        display: false
                    },
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            title: function (context) {
                                return context[0].label;
                            },
                            label: function (context) {
                                return context.dataset.label + ': ' + context.parsed.y + ' spells';
                            }
                        }
                    }
                }
            }
        });
    });