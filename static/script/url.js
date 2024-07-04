//======全局变量======
let chosen_url;//用户输入url
let chosen_platform;//用户选择平台
//======全局变量======

function init_url() {
    chosen_url = null;
    chosen_platform = 0;
    document.getElementById('platformChose').value = null;
    document.getElementById('urlInput').value = null;
    init_data_post();
    init_urlInfo();
}

//url输入监听
function init_urlInfo() {
    document.getElementById('platformChose').addEventListener('input', function (event) {
        chosen_platform = event.target.value;
    });
    document.getElementById('urlInput').addEventListener('input', function (event) {
        chosen_url = event.target.value;
    });
}

//url提交
function urlSubmit() {
    let url_post = {
        url: chosen_url,
        platform: chosen_platform
    };
    chosen_url = null;
    chosen_platform = null;
    document.getElementById('platformChose').value = null;
    document.getElementById('urlInput').value = null;

    // 改
    fetch('http://127.0.0.1:3000', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(url_post)
    })
        .then(response => response.json())
        .then(backdata => {
            console.log(backdata);
            let imgctr = document.getElementById('image-ctr');

            imgctr.innerHTML = `<img class="img-thumbnail" src="data:image/png;base64, ${backdata.img}">`;


            // 信息表格
            infoctr = document.getElementById('ctr-table-info');
            euser_info = ``;
            for (let i = 0; i < data.sex.length; ++i) {
                let type = "";
                if (i % 2 === 1) {
                    type = "bg bg-primary";
                } else type = "";
                euser_info +=
                    ` <tr class="${type}">
                <td>${i + 1}</td>
                <td>${data.sex[i]}</td>
                <td>${data.level[i]}</td>
                <td>${data.item_cnt[i]}</td>
                <td>${data.price[i]}</td> </tr>
                `;
            }

            infoctr.innerHTML += `                            
                            <table class="table table-dark mb-0">
                                <thead>
                                    <tr>
                                        <th scope="col">#</th>
                                        <th scope="col">用户性别</th>
                                        <th scope="col">用户等级</th>
                                        <th scope="col">优惠项数</th>
                                        <th scope="col">商品价格</th>
                                    </tr>
                                </thead> <tbody> 
                                ` + euser_info + `</tbody>    </table>`;


            // 历史信息表格
            euser_his = ``;
            for (let i = 0; i < data.sex.length; ++i) {
                let type = "";
                if (i % 2 === 1) {
                    type = "bg bg-primary";
                } else type = "";
                euser_his +=
                    `                 
                    <tr class="${type}">
                    <th scope="row">${i+1}</th>
                    <td>${data.platform[i]}</td>
                    <td>${data.detect_time[i]}</td>
                    <td>${data.info[i]}</td>
                    <td>${data.max_price[i]}</td>
                    <td>${data.min_price[i]}</td>
                    <td>${data.percent[i]}</td>
                </tr>
                `;
            }

            hisctr = document.getElementById('ctr-table-history');
            hisctr.innerHTML += `<table class="table table-dark mb-0">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">平台</th>
                    <th scope="col">检测时间</th>
                    <th scope="col">商品信息</th>
                    <th scope="col">最高价格</th>
                    <th scope="col">最低价格</th>
                    <th scope="col">高于平均价格率</th>
                </tr>
            </thead>
            <tbody>` + euser_his + `
            </tbody>
        </table>`
        })
}

//初始化数据请求
function init_data_post() {
    fetch('http://127.0.0.1:5000/init_homepage', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.text())
        .then(backdata => {
            let data = JSON.parse(backdata);
            console.log(data);
            let choseList = document.getElementById('platformChose');

            //将平台名称设置到选择栏
            data.platform_list.forEach(function (item, index) {
                var optionElement = document.createElement("option");
                optionElement.value = index;
                optionElement.textContent = item;
                choseList.appendChild(optionElement);
            });
        });
}
