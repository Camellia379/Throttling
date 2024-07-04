function init_olstatus(oldata) {
    new Chart(document.getElementById("ol-status"), {
        type: 'line',
        data: {
            labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
            datasets: oldata
        },
        options: {
            title: {
                display: true,
                text: 'x小时前仿真用户数量统计'
            }
        }
    });
}

function init_euser() {
    init_data();
}

function init_data(){
    
    fetch('http://127.0.0.1:5000/euser_info', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.text())
        .then(backdata => {
            let data = JSON.parse(backdata);
            let statistic = [{
                data: data.online_cnt,
                label: "在线数量",
                borderColor: "rgba(118,139,244,1.000)",
                backgroundColor: "rgba(118,139,244,0.500)",
                fill: true
            }, {
                data: data.work_time,
                label: "工作时长",
                borderColor: "rgba(255, 240, 34, 1.000)",
                backgroundColor: "rgba(255, 240, 34, 0.500)",
                fill: true
            },
            ];
            // 渲染折线图
            init_olstatus(statistic);

            //渲染表格
            let euser_ctr = document.getElementById('euser-ctr');
            euser_info_ = ``;
            for(let i = 0; i < data.item_cnt.length;++i){
                let type = "";
                if (i % 2 === 1) {
                    type = "bg bg-primary";
                } else type = "";
                euser_info_ += `
                    <tr class="${type}">
                        <td>${i+1}</td>
                        <td>${data.sex[i]}</td>
                        <td>${data.level[i]}</td>
                        <td>${data.item_cnt[i]}</td>
                        <td>${data.online_status[i]}</td>
                    </tr>
                `;
            }

            euser_ctr.innerHTML += `                                
                                <table class="table table-dark mb-0" id="euserinfo">
                                    <thead>
                                        <tr>
                                            <th scope="col">#</th>
                                            <th scope="col">用户性别</th>
                                            <th scope="col">用户等级</th>
                                            <th scope="col">优惠数量</th>
                                            <th scope="col">在线状态</th>
                                        </tr>
                                    </thead>
                                    <tbody>`+ euser_info_ +`</tbody>
                                </table>`
        })
}