// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    searching:false, //去掉搜索框
    bLengthChange:false,//去掉每页多少条框体
  });
});
