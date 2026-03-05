// dashboard/charts.js

// Using Chart.js to render data visualizations
// Sample aggregated mock dataset simulating real trends from the Indian Accident Dataset

document.addEventListener("DOMContentLoaded", () => {

    // Colors for graphs
    const chartColors = ['#0d6efd', '#dc3545', '#ffc107', '#0dcaf0', '#6f42c1', '#20c997'];

    // 1. Severity Distribution
    const ctxSeverity = document.getElementById('severityChart').getContext('2d');
    new Chart(ctxSeverity, {
        type: 'doughnut',
        data: {
            labels: ['Minor', 'Serious', 'Fatal'],
            datasets: [{
                data: [32495, 8451, 1204],
                backgroundColor: ['#0dcaf0', '#ffc107', '#dc3545'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });

    // 2. Weather Conditions vs Accidents
    const ctxWeather = document.getElementById('weatherChart').getContext('2d');
    new Chart(ctxWeather, {
        type: 'bar',
        data: {
            labels: ['Fine', 'Raining', 'Fog/Mist', 'Snowing', 'High Winds'],
            datasets: [{
                label: 'Number of Accidents',
                data: [25000, 11500, 3200, 1400, 1050],
                backgroundColor: 'rgba(13, 110, 253, 0.7)',
                borderColor: '#0d6efd',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // 3. Road Type Distribution
    const ctxRoadType = document.getElementById('roadTypeChart').getContext('2d');
    new Chart(ctxRoadType, {
        type: 'bar',
        data: {
            labels: ['Single carriageway', 'Dual carriageway', 'Roundabout', 'One way', 'Slip road'],
            datasets: [{
                label: 'Accidents',
                data: [28000, 9200, 3100, 1000, 850],
                backgroundColor: 'rgba(111, 66, 193, 0.7)',
                borderColor: '#6f42c1',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y', // Makes it a horizontal bar chart
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { beginAtZero: true }
            }
        }
    });

    // 4. Time of Day Trends
    const ctxTimeOfDay = document.getElementById('timeOfDayChart').getContext('2d');
    new Chart(ctxTimeOfDay, {
        type: 'line',
        data: {
            labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
            datasets: [{
                label: 'Accident Frequency',
                data: [1200, 800, 6500, 4300, 8900, 3500], // Spikes at rush hour (8AM and 4PM)
                backgroundColor: 'rgba(220, 53, 69, 0.2)',
                borderColor: '#dc3545',
                borderWidth: 2,
                fill: true,
                tension: 0.4 // Gives it a smooth curve
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
});
