(function (){
    const btnDelete = document.querySelectorAll('.btnDelete');

    btnDelete.forEach(btn => {
        btn.addEventListener('click', (e) => {
        const confirmacion = confirm('¿Estás seguro de eliminar este registro?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();