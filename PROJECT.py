<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time Disaster Alert System</title>
    <style>
        Body {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            min-height: 100%;
            color: #333;
        }

        html {
            height: 100%;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            min-height: 100%;
        }

        .header {
            text-align: center;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
        }

        .title {
            font-size: 2.5em;
            color: #1e3c72;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .subtitle {
            font-size: 1.2em;
            color: #666;
            margin-bottom: 20px;
        }

        .status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(135deg, #28a745, #20c997);
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
        }

        .status-item {
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: bold;
        }

        .pulse {
            width: 12px;
            height: 12px;
            background: #fff;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
        }

        .main-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            margin-bottom: 25px;
        }

        .panel {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
        }

        .panel-title {
            font-size: 1.5em;
            color: #1e3c72;
            margin-bottom: 20px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #333;
        }

        .form-input, .form-select {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1em;
            transition: all 0.3s ease;
            box-sizing: border-box;
        }

        .form-input:focus, .form-select:focus {
            outline: none;
            border-color: #1e3c72;
            box-shadow: 0 0 0 3px rgba(30, 60, 114, 0.1);
        }

        .severity-slider {
            width: 100%;
            height: 8px;
            border-radius: 5px;
            background: linear-gradient(to right, #28a745, #ffc107, #fd7e14, #dc3545);
            outline: none;
            -webkit-appearance: none;
        }

        .severity-slider::-webkit-slider-thumb {
            appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #fff;
            border: 3px solid #1e3c72;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }

        .severity-labels {
            display: flex;
            justify-content: space-between;
            margin-top: 8px;
            font-size: 0.9em;
            color: #666;
        }

        .submit-btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #dc3545, #c82333);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(220, 53, 69, 0.4);
        }

        .submit-btn:disabled {
            background: #6c757d;
            cursor: not-allowed;
            transform: none;
        }

        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 25px;
        }

        .metric-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }

        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
        }

        .metric-icon {
            font-size: 3em;
            margin-bottom: 10px;
        }

        .metric-value {
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .metric-label {
            font-size: 1em;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .alerts-container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            max-height: 500px;
            overflow-y: auto;
        }

        .alert-item {
            background: #fff;
            border-left: 5px solid;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            animation: slideIn 0.5s ease;
        }

        .alert-item.severity-1 { border-left-color: #28a745; }
        .alert-item.severity-2 { border-left-color: #ffc107; }
        .alert-item.severity-3 { border-left-color: #fd7e14; }
        .alert-item.severity-4 { border-left-color: #dc3545; }

        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }

        .alert-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }

        .alert-type {
            font-weight: bold;
            font-size: 1.1em;
            color: #1e3c72;
        }

        .alert-time {
            font-size: 0.9em;
            color: #666;
        }

        .alert-location {
            color: #666;
            margin-bottom: 10px;
        }

        .resource-allocation {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }

        .resource-tag {
            background: linear-gradient(135deg, #17a2b8, #138496);
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.9em;
            font-weight: bold;
        }

        .map-container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            text-align: center;
            min-height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .map-placeholder {
            width: 100%;
            height: 250px;
            background: linear-gradient(135deg, #e3f2fd, #bbdefb);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2em;
            color: #1976d2;
            border: 2px dashed #1976d2;
        }

        .prediction-panel {
            background: linear-gradient(135deg, #6f42c1, #5a32a3);
            color: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(111, 66, 193, 0.3);
        }

        .prediction-title {
            font-size: 1.5em;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .prediction-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            backdrop-filter: blur(10px);
        }

        .prediction-label {
            font-weight: bold;
            margin-bottom: 5px;
        }

        .prediction-value {
            font-size: 1.2em;
            color: #ffd700;
        }

        @media (max-width: 768px) {
            .main-grid {
                grid-template-columns: 1fr;
            }
            
            .dashboard-grid {
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            }
            
            .title {
                font-size: 2em;
            }
            
            .status-bar {
                flex-direction: column;
                gap: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="title">🚨 Disaster Alert & Resource System</h1>
            <p class="subtitle">Real-Time Emergency Response Platform</p>
        </div>

        <div class="status-bar">
            <div class="status-item">
                <div class="pulse"></div>
                <span>System Status: ACTIVE</span>
            </div>
            <div class="status-item">
                <span>🌐 Connected Sensors: 247</span>
            </div>
            <div class="status-item">
                <span>⚡ Last Update: <span id="lastUpdate">Just now</span></span>
            </div>
        </div>

        <div class="main-grid">
            <div class="panel">
                <h2 class="panel-title">📋 Report New Incident</h2>
                <form id="incidentForm">
                    <div class="form-group">
                        <label class="form-label">Disaster Type</label>
                        <select class="form-select" id="disasterType" required>
                            <option value="">Select disaster type...</option>
                            <option value="flood">🌊 Flood</option>
                            <option value="earthquake">🏔️ Earthquake</option>
                            <option value="fire">🔥 Wildfire</option>
                            <option value="storm">⛈️ Storm/Hurricane</option>
                            <option value="landslide">🏔️ Landslide</option>
                            <option value="tornado">🌪️ Tornado</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Location</label>
                        <input type="text" class="form-input" id="location" placeholder="Enter city, state or coordinates" required>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Severity Level: <span id="severityValue">2</span></label>
                        <input type="range" class="severity-slider" id="severity" min="1" max="4" value="2" oninput="updateSeverity(this.value)">
                        <div class="severity-labels">
                            <span>Low</span>
                            <span>Moderate</span>
                            <span>High</span>
                            <span>Critical</span>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Affected Population (Estimated)</label>
                        <input type="number" class="form-input" id="population" placeholder="Number of people affected" min="1" required>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Additional Details</label>
                        <textarea class="form-input" id="details" rows="3" placeholder="Describe the situation, casualties, infrastructure damage, etc."></textarea>
                    </div>

                    <button type="submit" class="submit-btn" id="submitBtn">
                        🚨 Submit Emergency Report
                    </button>
                </form>
            </div>

            <div class="prediction-panel">
                <h2 class="prediction-title">🤖 AI Resource Predictions</h2>
                <div id="predictions">
                    <div class="prediction-item">
                        <div class="prediction-label">Select an incident type to see AI predictions</div>
                        <div class="prediction-value">Waiting for input...</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="dashboard-grid">
            <div class="metric-card">
                <div class="metric-icon">🚨</div>
                <div class="metric-value" style="color: #dc3545;" id="activeAlerts">0</div>
                <div class="metric-label">Active Alerts</div>
            </div>
            <div class="metric-card">
                <div class="metric-icon">🚑</div>
                <div class="metric-value" style="color: #28a745;" id="ambulancesDeployed">0</div>
                <div class="metric-label">Ambulances Deployed</div>
            </div>
            <div class="metric-card">
                <div class="metric-icon">👥</div>
                <div class="metric-value" style="color: #17a2b8;" id="rescueTeams">0</div>
                <div class="metric-label">Rescue Teams</div>
            </div>
            <div class="metric-card">
                <div class="metric-icon">📦</div>
                <div class="metric-value" style="color: #ffc107;" id="suppliesAllocated">0</div>
                <div class="metric-label">Supply Packages</div>
            </div>
        </div>

        <div class="main-grid">
            <div class="alerts-container">
                <h2 class="panel-title">📢 Live Incident Feed</h2>
                <div id="alertsFeed">
                    <div class="alert-item severity-2">
                        <div class="alert-header">
                            <span class="alert-type">🌊 Flood Warning</span>
                            <span class="alert-time">2 min ago</span>
                        </div>
                        <div class="alert-location">📍 Houston, TX</div>
                        <div>Moderate flooding reported in downtown area. Water levels rising.</div>
                        <div class="resource-allocation">
                            <span class="resource-tag">🚑 3 Ambulances</span>
                            <span class="resource-tag">🚤 2 Rescue Boats</span>
                            <span class="resource-tag">📦 50 Relief Kits</span>
                        </div>
                    </div>
                    <div class="alert-item severity-3">
                        <div class="alert-header">
                            <span class="alert-type">🔥 Wildfire Alert</span>
                            <span class="alert-time">15 min ago</span>
                        </div>
                        <div class="alert-location">📍 Los Angeles, CA</div>
                        <div>High severity wildfire spreading rapidly. Evacuations in progress.</div>
                        <div class="resource-allocation">
                            <span class="resource-tag">🚁 5 Helicopters</span>
                            <span class="resource-tag">🚒 8 Fire Trucks</span>
                            <span class="resource-tag">👥 12 Rescue Teams</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="map-container">
                <h2 class="panel-title">🗺️ Real-Time Incident Map</h2>
                <div class="map-placeholder">
                    <div>
                        <div style="font-size: 3em; margin-bottom: 10px;">🗺️</div>
                        <div>Interactive Map View</div>
                        <div style="font-size: 0.9em; margin-top: 10px; color: #666;">
                            Incidents plotted by location and severity
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Resource allocation algorithms based on disaster type and severity
        const resourceAlgorithms = {
            flood: {
                ambulances: (population, severity) => Math.ceil((population / 1000) * severity * 0.8),
                rescueTeams: (population, severity) => Math.ceil((population / 2000) * severity * 1.2),
                supplies: (population, severity) => Math.ceil((population / 100) * severity * 1.5),
                boats: (population, severity) => Math.ceil((population / 5000) * severity * 2),
                helicopters: (population, severity) => Math.max(1, Math.ceil((population / 10000) * severity))
            },
            earthquake: {
                ambulances: (population, severity) => Math.ceil((population / 800) * severity * 1.2),
                rescueTeams: (population, severity) => Math.ceil((population / 1500) * severity * 1.5),
                supplies: (population, severity) => Math.ceil((population / 80) * severity * 2),
                searchDogs: (population, severity) => Math.ceil((population / 8000) * severity * 3),
                heavyEquipment: (population, severity) => Math.ceil((population / 15000) * severity * 2)
            },
            fire: {
                ambulances: (population, severity) => Math.ceil((population / 1200) * severity * 0.9),
                rescueTeams: (population, severity) => Math.ceil((population / 2500) * severity * 1.1),
                supplies: (population, severity) => Math.ceil((population / 120) * severity * 1.3),
                firetrucks: (population, severity) => Math.ceil((population / 3000) * severity * 2),
                helicopters: (population, severity) => Math.ceil((population / 8000) * severity * 1.5)
            },
            storm: {
                ambulances: (population, severity) => Math.ceil((population / 1500) * severity * 0.7),
                rescueTeams: (population, severity) => Math.ceil((population / 3000) * severity * 1),
                supplies: (population, severity) => Math.ceil((population / 150) * severity * 1.8),
                shelters: (population, severity) => Math.ceil((population / 500) * severity * 1.2),
                generators: (population, severity) => Math.ceil((population / 2000) * severity * 1)
            },
            landslide: {
                ambulances: (population, severity) => Math.ceil((population / 1000) * severity * 1.1),
                rescueTeams: (population, severity) => Math.ceil((population / 1800) * severity * 1.4),
                supplies: (population, severity) => Math.ceil((population / 90) * severity * 1.6),
                heavyEquipment: (population, severity) => Math.ceil((population / 12000) * severity * 2.5),
                searchDogs: (population, severity) => Math.ceil((population / 6000) * severity * 2)
            },
            tornado: {
                ambulances: (population, severity) => Math.ceil((population / 900) * severity * 1.3),
                rescueTeams: (population, severity) => Math.ceil((population / 2000) * severity * 1.3),
                supplies: (population, severity) => Math.ceil((population / 100) * severity * 2),
                shelters: (population, severity) => Math.ceil((population / 400) * severity * 1.5),
                searchDogs: (population, severity) => Math.ceil((population / 7000) * severity * 1.8)
            }
        };

        let alertCount = 2;
        let totalAmbulances = 11;
        let totalRescueTeams = 20;
        let totalSupplies = 62;

        // Update severity display
        function updateSeverity(value) {
            document.getElementById('severityValue').textContent = value;
            updatePredictions();
        }

        // Update predictions based on current form values
        function updatePredictions() {
            const disasterType = document.getElementById('disasterType').value;
            const population = parseInt(document.getElementById('population').value) || 0;
            const severity = parseInt(document.getElementById('severity').value);

            const predictionsContainer = document.getElementById('predictions');

            if (!disasterType || !population) {
                predictionsContainer.innerHTML = `
                    <div class="prediction-item">
                        <div class="prediction-label">Complete the form to see AI predictions</div>
                        <div class="prediction-value">Waiting for input...</div>
                    </div>
                `;
                return;
            }

            const algorithm = resourceAlgorithms[disasterType];
            if (!algorithm) return;

            let predictionsHTML = '';
            for (const [resource, calculator] of Object.entries(algorithm)) {
                const amount = calculator(population, severity);
                const resourceNames = {
                    ambulances: '🚑 Ambulances',
                    rescueTeams: '👥 Rescue Teams',
                    supplies: '📦 Supply Packages',
                    boats: '🚤 Rescue Boats',
                    helicopters: '🚁 Helicopters',
                    searchDogs: '🐕 Search Dogs',
                    heavyEquipment: '🚜 Heavy Equipment',
                    firetrucks: '🚒 Fire Trucks',
                    shelters: '🏠 Emergency Shelters',
                    generators: '⚡ Generators'
                };

                predictionsHTML += `
                    <div class="prediction-item">
                        <div class="prediction-label">${resourceNames[resource] || resource}</div>
                        <div class="prediction-value">${amount} units</div>
                    </div>
                `;
            }

            predictionsContainer.innerHTML = predictionsHTML;
        }

        // Handle form submission
        document.getElementById('incidentForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const submitBtn = document.getElementById('submitBtn');
            submitBtn.disabled = true;
            submitBtn.textContent = '🔄 Processing...';

            // Get form data
            const disasterType = document.getElementById('disasterType').value;
            const location = document.getElementById('location').value;
            const severity = parseInt(document.getElementById('severity').value);
            const population = parseInt(document.getElementById('population').value);
            const details = document.getElementById('details').value;

            // Simulate processing delay
            setTimeout(() => {
                // Add new alert to feed
                addNewAlert(disasterType, location, severity, population, details);
                
                // Update metrics
                updateMetrics(disasterType, severity, population);
                
                // Reset form
                document.getElementById('incidentForm').reset();
                document.getElementById('severityValue').textContent = '2';
                updatePredictions();
                
                // Reset button
                submitBtn.disabled = false;
                submitBtn.textContent = '🚨 Submit Emergency Report';
                
                // Show success message
                showNotification('✅ Incident reported successfully! Resources are being allocated.', 'success');
                
            }, 2000);
        });

        // Add new alert to the feed
        function addNewAlert(type, location, severity, population, details) {
            const alertsFeed = document.getElementById('alertsFeed');
            const typeEmojis = {
                flood: '🌊',
                earthquake: '🏔️',
                fire: '🔥',
                storm: '⛈️',
                landslide: '🏔️',
                tornado: '🌪️'
            };

            const typeNames = {
                flood: 'Flood Alert',
                earthquake: 'Earthquake Alert',
                fire: 'Wildfire Alert',
                storm: 'Storm Alert',
                landslide: 'Landslide Alert',
                tornado: 'Tornado Alert'
            };

            // Calculate resources
            const algorithm = resourceAlgorithms[type];
            let resourceTags = '';
            
            if (algorithm) {
                const resources = Object.entries(algorithm).slice(0, 3); // Show first 3 resources
                resources.forEach(([resource, calculator]) => {
                    const amount = calculator(population, severity);
                    const resourceNames = {
                        ambulances: '🚑 Ambulances',
                        rescueTeams: '👥 Rescue Teams',
                        supplies: '📦 Relief Kits',
                        boats: '🚤 Rescue Boats',
                        helicopters: '🚁 Helicopters',
                        searchDogs: '🐕 Search Dogs',
                        heavyEquipment: '🚜 Heavy Equipment',
                        firetrucks: '🚒 Fire Trucks',
                        shelters: '🏠 Shelters',
                        generators: '⚡ Generators'
                    };
                    
                    resourceTags += `<span class="resource-tag">${resourceNames[resource] || resource} ${amount}</span>`;
                });
            }

            const alertHTML = `
                <div class="alert-item severity-${severity}">
                    <div class="alert-header">
                        <span class="alert-type">${typeEmojis[type]} ${typeNames[type]}</span>
                        <span class="alert-time">Just now</span>
                    </div>
                    <div class="alert-location">📍 ${location}</div>
                    <div>${details || `${typeNames[type]} reported. Population affected: ${population.toLocaleString()}`}</div>
                    <div class="resource-allocation">
                        ${resourceTags}
                    </div>
                </div>
            `;

            alertsFeed.insertAdjacentHTML('afterbegin', alertHTML);
            alertCount++;
        }

        // Update dashboard metrics
        function updateMetrics(type, severity, population) {
            const algorithm = resourceAlgorithms[type];
            if (algorithm) {
                if (algorithm.ambulances) {
                    totalAmbulances += algorithm.ambulances(population, severity);
                }
                if (algorithm.rescueTeams) {
                    totalRescueTeams += algorithm.rescueTeams(population, severity);
                }
                if (algorithm.supplies) {
                    totalSupplies += algorithm.supplies(population, severity);
                }
            }

            // Update display with animation
            animateCounter('activeAlerts', alertCount);
            animateCounter('ambulancesDeployed', totalAmbulances);
            animateCounter('rescueTeams', totalRescueTeams);
            animateCounter('suppliesAllocated', totalSupplies);
        }

        // Animate counter updates
        function animateCounter(elementId, targetValue) {
            const element = document.getElementById(elementId);
            const currentValue = parseInt(element.textContent);
            const increment = Math.ceil((targetValue - currentValue) / 20);
            
            let current = currentValue;
            const timer = setInterval(() => {
                current += increment;
                if (current >= targetValue) {
                    current = targetValue;
                    clearInterval(timer);
                }
                element.textContent = current;
            }, 50);
        }

        // Show notification
        function showNotification(message, type) {
            const notification = document.createElement('div');
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: ${type === 'success' ? '#28a745' : '#dc3545'};
                color: white;
                padding: 15px 25px;
                border-radius: 8px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                z-index: 1000;
                animation: slideIn 0.5s ease;
            `;
            notification.textContent = message;
            document.body.appendChild(notification);

            setTimeout(() => {
                notification.remove();
            }, 4000);
        }

        // Update last update time
        function updateLastUpdateTime() {
            const now = new Date();
            const timeString = now.toLocaleTimeString();
            document.getElementById('lastUpdate').textContent = timeString;
        }

        // Add event listeners
        document.getElementById('disasterType').addEventListener('change', updatePredictions);
        document.getElementById('population').addEventListener('input', updatePredictions);
        document.getElementById('severity').addEventListener('input', updatePredictions);

        // Initialize
        updatePredictions();
        setInterval(updateLastUpdateTime, 30000); // Update every 30 seconds

        // Simulate real-time updates
        setInterval(() => {
            // Randomly add new incidents for demonstration
            if (Math.random() < 0.1) { // 10% chance every 10 seconds
                const types = ['flood', 'fire', 'storm', 'earthquake'];
                const locations = ['Miami, FL', 'Phoenix, AZ', 'Seattle, WA', 'Denver, CO', 'Atlanta, GA'];
                const randomType = types[Math.floor(Math.random() * types.length)];
                const randomLocation = locations[Math.floor(Math.random() * locations.length)];
                const randomSeverity = Math.floor(Math.random() * 3) + 1;
                const randomPopulation = Math.floor(Math.random() * 5000) + 500;
                
                addNewAlert(randomType, randomLocation, randomSeverity, randomPopulation, 'Automated sensor detection');
                updateMetrics(randomType, randomSeverity, randomPopulation);
                updateLastUpdateTime();
            }
        }, 10000);
    </script>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'98d5186f21bcbdd5',t:'MTc2MDI1NjM2MS4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>s