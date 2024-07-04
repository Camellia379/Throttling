function postInit() {
    console.log('init_now');
    let init_post = {
        info: 'init'
    };

    fetch('http://127.0.0.1:5000/test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(init_post)
    })
        .then(response => response.text())
        .then(backdata => {
            let data = JSON.parse(backdata);
            let element = document.getElementById('init_test');
            console.log(data);
            element.innerHTML = data.message;
        })
}