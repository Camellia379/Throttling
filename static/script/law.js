let defaultInfo = {
    name: "artemis",    //消费者姓名
    phn: "000-0000-0000",   //消费者电话
    id: "000000000000000000",    //消费者身份证号码
    ocur_time: "2024-01-01T00:00:00",     //发生日期
    gri_type: "default",     //申诉类型
    description: "null",     //描述
    evi: "null",     //证据
    relate_company: "null",      //涉及企业、组织s
}

let griInfo = defaultInfo;

function init_law() {
    addListener(); 
    isAllowSubmit(true);
}

function addListener() {
    document.getElementById('name').addEventListener('input', function (event) {
        griInfo.name = event.target.value;
        console.log(JSON.stringify(griInfo));
    });

    document.getElementById('phn').addEventListener('input', function (event) {
        griInfo.phn = event.target.value;
    });

    document.getElementById('id').addEventListener('input', function (event) {
        griInfo.id = event.target.value;
    });

    document.getElementById('time').addEventListener('input', function (event) {
        griInfo.ocur_time = event.target.value;
    });

    document.getElementById('relate_company').addEventListener('input', function (event) {
        griInfo.relate_company = event.target.value;
    });

    document.getElementById('gri_type').addEventListener('input', function (event) {
        griInfo.gri_type = event.target.value;
    });

    document.getElementById('description').addEventListener('input', function (event) {
        griInfo.description = event.target.value;
    });
}

function clear() {
    let namectr = document.getElementById('name');
    let phnctr = document.getElementById('phn');
    let idctr = document.getElementById('id');
    let ocur_timectr = document.getElementById('time');
    let gri_typectr = document.getElementById('gri_type');
    let description = document.getElementById('description');
    let relate_company = document.getElementById('relate_company');

    namectr.value = null;
    phnctr.value = null;
    idctr.value = null;
    ocur_timectr.value = "2024-01-01T00:00:00";
    gri_typectr.value = null;
    description.value = null;
    relate_company.value = null;
    griInfo = defaultInfo;
}

function isAllowSubmit(allow) {
    let savectr = document.getElementById('savegri');
    let subctr = document.getElementById('submitgri');
    savectr.disabled = allow;
    subctr.disabled = allow;
}

function generate() {
    alert('信息已提交');
    console.log(defaultInfo)
    // 改
    fetch('http://127.0.0.1:5000/generate_report', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(griInfo)
    })
        .then(response => response.text())
        .then(backdata => {
            clear();
            let data = JSON.parse(backdata);
            console.log(data);
            let container = document.getElementById('report-table');
            let report_template = `
                        <div class="table-responsive">
                                <div class="p-4 border shadow-sm rounded">
                                    <table class="table">
                                        <thead>
                                            <tr>
                                                <th scope="col">申诉人</th>
                                                <th scope="col">联系方式</th>
                                                <th scope="col">身份证号</th>
                                                <th scope="col">申诉类型</th>
                                                <th scope="col">涉及平台</th>
                                                <th scope="col">发生时间</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>${data.name}</td>
                                                <td>${data.phn}</td>
                                                <td>${data.id}</td>
                                                <td>${data.gri_type}</td>
                                                <td>${data.relate_company}</td>
                                                <td>${data.ocur_time}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <hr>
                                    <div class="row">
                                        <div class="col-md-6 border-right">
                                            <ul class="list-style-none">
                                                <li class="my-2 border-bottom pb-3">
                                                    <span class="font-weight-medium text-dark"><i
                                                            class="icon-note mr-2 text-success"></i>相关法律条款</span>
                                                </li>
                                                <li class="my-3">
                                                    <span><i class="icon-pencil mr-2 text-success"></i>${data.law}</span>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-6">
                                            <ul class="list-style-none">
                                                <li class="my-2 border-bottom pb-3">
                                                    <span class="font-weight-medium text-dark"><i
                                                            class="icon-note mr-2 text-danger"></i> 申诉描述 </span>
                                                </li>
                                                <li class="my-3">
                                                    <span><i class="icon-pencil mr-2 text-danger"></i>${data.description}</span>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>`;
            container.innerHTML += report_template;
        })
}
