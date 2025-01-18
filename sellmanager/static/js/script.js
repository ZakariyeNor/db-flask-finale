document.addEventListener('DOMContentLoaded', function() {
    let picker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(picker, {
        format: "dd mmmm yyyy",
        i18n: {done: "select"}
    });
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    let collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);
  });