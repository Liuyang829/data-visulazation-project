<template>
  <div id="app">
    <div id="main" class="child" style="width: 1200px; height: 700px"></div>
  </div>
</template>

<script>
export default {
  name: "app",
  methods: {
    drawChart() {
      console.log(11111)
      // import * as echarts from "echarts"
      var appData = require("./assets/test6.json");
      var formatUtil = this.$echarts.format;
      // 基于准备好的dom，初始化echarts实例
      let myChart = this.$echarts.init(document.getElementById("main"));
      // 指定图表的配置项和数据
      let option = {
        title: {
            text: 'Wikipedia article classes',
            left: 'center'
        },
        tooltip: {
          // trigger: "item",
          // triggeron: "mousemove",
          formatter: function (info) {
            // console.log(info);
            var value = info.value;
            var treePathInfo = info.treePathInfo;
            var treePath = [];
            // console.log(value)
            for (var i = 1; i < treePathInfo.length; i++) {
              treePath.push(treePathInfo[i].name);
            }
            return [
              '<div class="tooltip-title">' +
                formatUtil.encodeHTML(treePath.join("/")) +
                "</div>",
              "Word count: " + formatUtil.addCommas(value),
            ].join("");
          },
        },
        series: [
          {
            type: "treemap",
            drillDownIcon: "",
            leafDepth: 2,
            label: {
              show: true,
              formatter: "{b}",
              color: "#ffffff",
            },
            upperLabel: {
              show: true,
              height: 20,
              color: "#ffffff",
            },
            // itemStyle: {
            //   borderColor: "#fff",
            // },
            levels: [
              {
                itemStyle: {
                  borderColor: "#CCCCCC",
                  borderWidth: 6,
                  gapWidth: 4,
                },
                upperLabel: {
                  show: false,
                },
              },
              {
                colorSaturation: [0.4, 0.6],
                itemStyle: {
                  borderColorSaturation: 0.7,
                  gapWidth: 3,
                  borderWidth: 2,
                },
              },
              {
                colorSaturation: [0.3, 0.5],
                itemStyle: {
                  borderColorSaturation: 0.6,
                  borderWidth: 1,
                  gapWidth: 3,
                },
              },
              {
                itemStyle: {
                  borderColorSaturation: 0.6,
                  gapWidth: 1,
                },
              },
            ],
            data: appData,
          },
        ],
      };
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    },
  },
  mounted() {
    this.drawChart();
  },
};
</script>


<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.child {
  /* width: 100px;
  height: 100px; */
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
}
</style>
