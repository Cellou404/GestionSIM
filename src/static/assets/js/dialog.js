;(function(){
    const modal = new bootstrap.Modal(document.getElementById('modal'))

    hx.on('htmx:afterSwap', (e) => {
        if (e.target.id === 'modalBody'){
            modal.show()
        }
    })
})