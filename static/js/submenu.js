document.querySelectorAll('ul#nav li').forEach(function(li) {
    li.addEventListener('mouseover', function() {
        this.querySelector('ul').style.display = 'block';
    });

    li.addEventListener('mouseout', function() {
        this.querySelector('ul').style.display = 'none';
    });
});