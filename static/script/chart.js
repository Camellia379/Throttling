function init_chart() {
    init_detect_sta(testdata1);
    init_cart_sta(testdata2);
    init_urlInfo();
}

let testdata1 = [{
    data: [
        273, 689, 341, 758, 910, 167, 450, 821, 135, 792,
        303, 502, 784, 196, 205, 847, 930, 612, 478, 391,
        564, 728, 110, 489
    ],
    label: "检出量",
    borderColor: "rgba(118,139,244,1.000)",
    backgroundColor: "rgba(118,139,244,0.600)",
    fill: true
}, {
    data: [
        923, 1719, 1422, 1212, 1399, 1598, 650, 921, 352, 1922,
        1223, 1010, 934, 991, 605, 1547, 1430, 912, 938, 3911,
        964, 1028, 452, 989
    ],
    label: "总检测量",
    borderColor: "rgba(255,79,122,1.000)",
    backgroundColor: "rgba(255,79,122,0.600)",
    fill: true
}
];

let testdata2 = {
    labels: ["携程旅行", "淘宝", "拼多多", "东方航空", "七天连锁酒店"],
    datasets: [
        {
            label: "检出杀熟次数",
            backgroundColor: [
                "#7161EF", 
                "#957FEF", 
                "#B79CED", 
                "#DEC0F1", 
                "#EFD9CE"
            ],
            data: [8478, 6267, 5534, 4784, 3433]
        }
    ]
};

function init_detect_sta(olcheck_data) {
    new Chart(document.getElementById("olcheck—times"), {
        type: 'line',
        data: {
            labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
            datasets: olcheck_data
        },
        options: {
            title: {
                display: true,
                text: 'x小时前在线检测总数量统计'
            }
        }
    });
}

function init_cart_sta(cart_data) {
    new Chart(document.getElementById("bar-chart-horizontal"), {
        type: 'horizontalBar',
        data: cart_data,
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: '最多检出软件'
            }
        }
    });
}

