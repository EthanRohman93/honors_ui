document.getElementById('calorieCalculator').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    const age = parseFloat(document.getElementById('age').value);
    const gender = document.getElementById('gender').value;
    const activityLevel = document.getElementById('activityLevel').value;
    
    let bmr;
    
    // Calculate Basal Metabolic Rate (BMR) using Mifflin-St Jeor Equation
    if (gender === 'male') {
        bmr = 10 * weight + 6.25 * height - 5 * age + 5;
    } else {
        bmr = 10 * weight + 6.25 * height - 5 * age - 161;
    }
    
    // Adjust BMR based on activity level
    let multiplier = 1.2; // sedentary
    if (activityLevel === 'lightly_active') {
        multiplier = 1.375;
    } else if (activityLevel === 'moderately_active') {
        multiplier = 1.55;
    } else if (activityLevel === 'very_active') {
        multiplier = 1.725;
    } else if (activityLevel === 'extra_active') {
        multiplier = 1.9;
    }
    
    const tdee = bmr * multiplier;
    
    document.getElementById('result').innerHTML = `Your maintenance calories: ${tdee.toFixed(2)} calories/day`;
});

