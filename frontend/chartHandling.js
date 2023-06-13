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

        let ctx = document.getElementById('chart').getContext('2d');
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