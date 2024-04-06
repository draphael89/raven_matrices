document.addEventListener('DOMContentLoaded', function() {
    var answerOptions = document.querySelectorAll('.answer-options input[type="radio"]');
    var submitButton = document.querySelector('.answer-options input[type="submit"]');

    submitButton.disabled = true;

    answerOptions.forEach(function(option) {
        option.addEventListener('change', function() {
            submitButton.disabled = false;
        });
    });

    document.querySelector('.answer-options form').addEventListener('submit', function(event) {
        event.preventDefault();

        var selectedOption = document.querySelector('.answer-options input[type="radio"]:checked');

        if (selectedOption) {
            var feedback = document.querySelector('.feedback');
            feedback.textContent = 'Checking...';
            feedback.classList.remove('correct', 'incorrect');
            feedback.style.opacity = 1;

            setTimeout(function() {
                event.target.submit();
            }, 1000);
        }
    });
});