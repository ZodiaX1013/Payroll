// Progress Bar 

var elem = document.getElementById("progress-bar");
var width = 1;
var id = {};

function progressBar() {

  id = setInterval(frame, 10);

  function frame() {
    if (width >= 100) {
      clearInterval(id);
    } else {
      width++;
      elem.style.width = width + '%'
      elem.innerHTML = width*1 + '%';
    }
  }
}

// ENd progressBar()

// Segment View

// "use strict";

// const body = document.body;
// const bgColorsBody = ["#ffb457", "#ff96bd", "#9999fb", "#ffe797", "#cffff1"];
// const menu = body.querySelector(".menu");
// const menuItems = menu.querySelectorAll(".menu__item");
// const menuBorder = menu.querySelector(".menu__border");
// let activeItem = menu.querySelector(".active");

// function clickItem(item, index) {
//   menu.style.removeProperty("--timeOut");

//   if (activeItem == item) return;

//   if (activeItem) {
//     activeItem.classList.remove("active");
//   }

//   item.classList.add("active");
//   body.style.backgroundColor = bgColorsBody[index];
//   activeItem = item;
//   offsetMenuBorder(activeItem, menuBorder);
// }

// function offsetMenuBorder(element, menuBorder) {
//   const offsetActiveItem = element.getBoundingClientRect();
//   const left =
//     Math.floor(
//       offsetActiveItem.left -
//         menu.offsetLeft -
//         (menuBorder.offsetWidth - offsetActiveItem.width) / 2
//     ) + "px";
// //   menuBorder.style.transform = `translate3d(${left}, 0 , 0)`;
// }

// offsetMenuBorder(activeItem, menuBorder);

// menuItems.forEach((item, index) => {
//   item.addEventListener("click", () => clickItem(item, index));
// });

// window.addEventListener("resize", () => {
//   offsetMenuBorder(activeItem, menuBorder);
//   menu.style.setProperty("--timeOut", "none");
// });

// Clear Function Of Form
function clearForm() {
  document.getElementById("emp").reset();
  // document.getElementById("emp2").reset();
  // document.getElementById("emp3").reset();
  // document.getElementById("emp4").reset();
}

function clearForm2() {
  // document.getElementById("eid").value = null
  // document.getElementById("pos").value = null
  // document.getElementById("lname").value = null
  // document.getElementById("fname").value = null
  document.getElementById("leave2").reset();
  
  // document.getElementById("emp").reset();
}

function clearForm3() {
  // document.getElementById("leave4").reset();
  document.getElementById("salary").reset();
  // document.getElementById("salary").reset();
  // document.getElementById("salary2").reset();
  // document.getElementById("salary3").reset();
  // document.getElementById("salary4").reset();
  // document.getElementById("salary5").reset();

  // document.getElementById("leave").reset();
  // document.getElementById("legal").reset();
  // document.getElementById("emp").reset();
}

// Save Button
function submitForms(){
  document.getElementById("emp").submit();
  // document.getElementById("emp2").submit();
  // document.getElementById("emp3").submit();
  // document.getElementById("emp4").submit();
}
function calculate()
// calculate = function()
{   
  // alert("Hello");
  
  // var temp, element = document.getElementById('efd')
  // if(element != null){
  //   str = element.value;
  //   alert(str)
  // }
  // else{
  //   alert("Null Value")
  // }
  var resources = document.getElementById('edf').value;
  var minutes = document.getElementById('month').value; 
  // alert(resources);
  // alert(minutes);
  // console.log(resources);
  // console.log(minutes);
  // document.getElementById('medf').value = parseFloat(resources) / parseFloat(minutes);
  document.getElementById('medf').value = parseInt(resources)/parseInt(minutes);
     
}
// function disable()
// {
//   var radio = document.getElementById("optradiod3")
//   if(radio.value == "Yes"){
//     document.getElementById("lwork").disabled = true;
//     alert("In If")
//   }
//   else{
//     document.getElementById("lwork").disabled = false;
//     alert("In ELse")
//   }

//   // document.getElementById('custom').disabled = false; 
//   // document.getElementById('charstype').disabled = true;

//   // document.getElementById('custom').disabled = true; 
//   // document.getElementById('charstype').disabled = false;
// }

// Hire Date Must Be Before Last Working Day
function checkDate()
{
  var hire = document.getElementById('hire').value
  var last = document.getElementById('lwork').value

  // alert(hire)
  // alert(last)
  if(last < hire){
    // alert("In If")
    document.getElementById("lwork").value = "";
    // alert("After")
  }
  // alert("Out If")
}

// End DAte

// multi level selection list

var $select1 = $( '#dep' ),
		$select2 = $( '#sdep' ),
    $options = $select2.find( 'option' );
    
$select1.on( 'change', function() {
	$select2.html( $options.filter( '[value="' + this.value + '"]' ) );
} ).trigger( 'change' );

// end selection list

// set % to 100

function percentage(){
  var per = document.getElementById("per").value

  if(per > 100){
    document.getElementById("per").value = 100
  }
  else{
    document.getElementById("per").value = per
  }
}
// end perdentage

// local and sick leave

function leave(){
  var local = document.getElementById("lleave").value
  var sick = document.getElementById("sleave").value

  if(local >365){
    document.getElementById("lleave").value = 365
  }
  else{
    document.getElementById("lleave").value = local
  }
  if(sick > 365){
    document.getElementById("sleave").value = 365
  }
  else{
    document.getElementById("sleave").value = sick
  }
}

// end leave

// Working Days

function days(){
  var days = document.getElementById("wday").value

  if(days > 30){
    document.getElementById("wday").value = 30
  }
  else{
    document.getElementById("wday").value = days
  }
}
//  End working

//  Next Employee ID

// function next(){
//   var emp = document.getElementById("eid")

// }

// end next

// Redirection Of Leave Page

function redirect() {
  let url = "http://127.0.0.1:5000/leave";
  window.location.href(url);
}

// End Of Redirection

// Gross Value
function grossvalue(){
  var basic = document.getElementById('basic').value;
  var arr = document.getElementById('arr').value;
  var over = document.getElementById('over').value;
  var travel = document.getElementById('travel').value;
  var other = document.getElementById('other').value;
  var car = document.getElementById('car').value;
  var medical = document.getElementById('med').value;


  var total = parseInt(basic)+parseInt(arr)+parseInt(over)+parseInt(travel)+parseInt(other)+parseInt(car)+parseInt(medical);
  // alert(total)
  document.getElementById('gross').value = Math.round(total)


}

function calculate2()
// calculate = function()
{   
  var edf = document.getElementById('edf').value;
  var month = document.getElementById('month').value; 
  var medf = parseInt(edf)/parseInt(month);
  document.getElementById('medf').value = Math.round(medf)
}

function payeCalc(){
  var basic = document.getElementById('basic').value
  var medf = document.getElementById('medf').value
  var gross = document.getElementById('gross').value
  var medical = document.getElementById('med').value
  var paye
  var csg
  var nsf
  var total = parseInt(gross) - parseInt(medf)
  if(basic > 50000){
    paye = total * 0.15
    document.getElementById('paye').value = Math.round(paye)

    csg = basic *0.03
    document.getElementById('csg').value = Math.round(csg)
  }
  else{
    paye = total * 0.1
    document.getElementById('paye').value = Math.round(paye)

    csg = basic *0.015
    document.getElementById('csg').value = Math.round(csg)

  } 
  nsf = basic * 0.01
  if(nsf > 213){
    nsf = 213
    document.getElementById('nsf').value = 213
  }
  else{
    document.getElementById('nsf').value = Math.round(nsf)
  }

  var levy = gross - medf - (3000000/13)
  var slevy1 = levy * 0.25

  var slevy2 = gross * 0.10
  var slevy
  if(slevy1 > slevy2){
    slevy = slevy2
    document.getElementById('levy').value = Math.round(slevy)
  }
  else{
    slevy = slevy1
    document.getElementById('levy').value = Math.round(slevy)
  }
  alert(gross)
  alert(paye)
  alert(csg)
  alert(nsf)
  alert(medical)
  alert(slevy)
  var net = gross - paye - csg - nsf - medical - slevy
  document.getElementById('net').value = Math.round(net)
}


// Calculate Tax and Other Data
function calculateSalary(){
  var basic = document.getElementById('bsal').value
  var car = document.getElementById('car').value
  var otherAllow = document.getElementById('oalw').value
  var overseas
  var tax = document.getElementById('amt1').value
  var ntax = document.getElementById('amt2').value
  var education = document.getElementById('edu').value
  var fixAllow = document.getElementById('falw').value

  overseas = parseInt(tax) + parseInt(ntax)

  var arrears = document.getElementById('arr').value
  var ot1 = document.getElementById('am1').value
  var ot2 = document.getElementById('am2').value
  var ot3 = document.getElementById('am3').value

  var overtime = parseInt(ot1) + parseInt(ot2) + parseInt(ot3)
  var travel = document.getElementById("travel").value
  var medical = document.getElementById('med2').value
  var edf = document.getElementById('edf').value
  
  var gross = parseInt(basic)  + parseInt(arrears) + parseInt(overtime) + parseInt(travel) + parseInt(otherAllow) + parseInt(tax) + parseInt(medical) + parseInt(car) + parseInt(fixAllow)
  var tgross = parseInt(basic)  + parseInt(arrears) + parseInt(overtime) + parseInt(travel) + parseInt(otherAllow) + parseInt(overseas) + parseInt(medical) + parseInt(fixAllow)
  
  var temp = basic * 0.06
  var payable
  if( temp > overseas)
  {
    payable = parseInt(gross)  - parseInt(car)
  }
  else
  {
    payable = parseInt(gross)  - parseInt(car) + parseInt(ntax)
  }
  

  var TIET = parseInt(edf) + parseInt(education)
  var IET = Math.round(TIET / 13)
  // alert(IET)
  // alert(IET)
  // alert(edf)
  // alert(education )
  // var IET = IET /13
  // alert(IET)
  // PAYE and CSG Calculation
  var tpaye
  var csg
  var paye
  if( basic > 50000 )
  {
    tpaye = (parseInt(gross) - parseInt(IET)) * 0.15
    // alert(paye)
    csg = Math.round( parseInt(basic) * 0.03 )
    paye = Math.round(tpaye)
  }
  else
  {
    paye = (parseInt(gross) - parseInt(IET)) * 0.1 
    csg = Math.round( parseInt(basic) * 0.015 )
    paye = Math.round(tpaye)
  }
  
  // NSF Calculation
  var nsf = parseInt(basic) * 0.01
  var ivbt = parseInt(basic) * 0.015
  if(nsf > 213)
  {
    nsf = 213
  }
  else
  {
    nsf = nsf
  }

  // NSF For Employer
  var ensf = parseInt(basic) * 0.025
  if(ensf > 513)
  {
    ensf = 513
  }
  else
  {
    ensf = ensf
  }

  // S.Levy Calculation

  var emo = parseInt(gross) * 13
  var levy
  var slevy
  if( emo > 3000000)
  {
    levy = ( parseInt(gross) - parseInt(IET) - (3000000/13) ) * 0.25
    var emo2 = parseInt(emo) * 0.1
    if(emo2 > levy)
    {
      slevy = Math.round(levy)
    }
    else
    {
      slevy = Math.round(emo2)
    }
  }
  else
  {
    slevy = 0
  }
  // alert(slevy)
  var deduction = Math.round(paye + csg + nsf)
  var net = Math.round(tgross - deduction)

  var pgross = document.getElementById("pgrs").value

  // Net Ch
  var netch = parseInt(gross) + parseInt(pgross) - parseInt(IET)
  document.getElementById("netch").value = netch


  // NPS
var nps
nps = parseInt(basic) * 0.06

  // Get Other Values
  var localRef = document.getElementById('lref').value
  
  var DiscBonus = document.getElementById('dbns').value
  var attendance = document.getElementById('atbns').value
  var transport = document.getElementById('tran').value
  var sick = document.getElementById('sref').value
  var special = document.getElementById('sbns').value
  var odeduction = document.getElementById('oded').value
  var late = document.getElementById('am4').value


  // Fill Readonly Field
  // fix allow
  document.getElementById('falw2').value = fixAllow
  document.getElementById('falw3').value = fixAllow
  // other deduction
  document.getElementById('oded2').value = odeduction
  // overtime
  document.getElementById('ot2').value = overtime
  document.getElementById('ot3').value = overtime
  // disc bonus
  document.getElementById('dbns2').value = DiscBonus
  document.getElementById('dbns3').value = DiscBonus
  // NSF
  document.getElementById('nsf').value = nsf
  document.getElementById('ivbt').value = Math.round(ivbt) 
  // other allow
  document.getElementById('oalw2').value = otherAllow
  document.getElementById('oalw3').value = otherAllow
  // taxable
  document.getElementById('txdes2').value = tax
  document.getElementById('txdes3').value = tax
  // transport
  document.getElementById('tran2').value = transport
  document.getElementById('tran3').value = transport
  // non taxable
  document.getElementById('ntxdes2').value = ntax
  // arrears
  document.getElementById('arr2').value = arrears
  document.getElementById('arr3').value = arrears
  // attendance
  document.getElementById('atbns2').value = attendance
  document.getElementById('atbns3').value = attendance
  // EOY
  document.getElementById('eoy').value = 0
  document.getElementById('eoy2').value = 0
  // loan
  document.getElementById('lrep').value = 0
  // leave refund 
  document.getElementById('lref2').value = localRef
  document.getElementById('lref3').value = localRef
  // paye
  document.getElementById('paye').value = paye
  document.getElementById('paye2').value = paye
  document.getElementById('paye3').value = paye
  // s.levy
  document.getElementById('levy').value = slevy
  // special bonus
  document.getElementById('spbonus2').value = special
  document.getElementById('spbonus3').value = special
  document.getElementById('spbonus4').value = special
  // lateness
  document.getElementById('late').value = late
  // NPS
  document.getElementById('nps').value = csg
  document.getElementById('nps2').value = Math.round(nps)
  document.getElementById('nsf2').value = Math.round(ensf)
  // IET
  document.getElementById('iet').value = IET
  // payable
  document.getElementById('pay').value = payable
  // Deduction
  document.getElementById('ded').value = deduction
  // Net Pay
  document.getElementById('npay').value = net
  // Gross
  document.getElementById('grs').value = gross
  // Current Gross
  document.getElementById('cgrs').value = gross

}


// function calculateSalary(){
//   var arr = document.getElementById('arr').value
//   var localRef = document.getElementById('lref').value
//   var fixAllow = document.getElementById('falw').value
//   var DiscBonus = document.getElementById('dbns').value
//   var AttBonus = document.getElementById('atbns').value
//   var transport = document.getElementById('tran').value
//   var sick = document.getElementById('sref').value
//   var speBonus = document.getElementById('sbns').value
  
//   var EOY = document.getElementById('eoy').value
//   var travel = document.getElementById('travel').value
//   // alert(speBonus)
//   var otherAllow = document.getElementById('oalw').value
//   var otherDeduction = document.getElementById('oded').value
  
//   var ot1 = document.getElementById('am1').value
//   var ot2 = document.getElementById('am2').value
//   var ot3 = document.getElementById('am3').value
//   var late = document.getElementById('am4').value
 
//   var tax = document.getElementById('amt1').value
//   var ntax = document.getElementById('amt2').value  
  
//   var medical = document.getElementById('med2').value
//   var car = document.getElementById('car').value
//   var edf = document.getElementById('edf').value
//   var loan = document.getElementById('lrep').value

  
//   var overseas
//   if(tax > 0 && ntax > 0){
//     overseas = parseInt(tax) + parseInt(ntax)
//   }
//   else{
//     tax = 0
//     ntax = 0
//     overseas = parseInt(tax) + parseInt(ntax)
//   }

//   var zero = 0
//   var overtime = parseInt(ot1) + parseInt(ot2) + parseInt(ot3)
//   if(overtime > 0){
//     document.getElementById('ot2').value = overtime
//   }
//   else{
//     document.getElementById('ot2').value = zero
//   }

//   document.getElementById('oalw2').value = otherAllow
//   document.getElementById('tran2').value = transport
//   document.getElementById('arr2').value = arr
//   document.getElementById('eoy').value = zero
//   document.getElementById('lref2').value = localRef
//   document.getElementById('spbonus2').value = speBonus
//   document.getElementById('falw2').value = fixAllow
//   document.getElementById('dbns2').value = DiscBonus
//   document.getElementById('txdes2').value = tax
//   document.getElementById('ntxdes2').value = ntax
//   document.getElementById('atbns2').value = AttBonus
//   document.getElementById('lrep').value = loan
//   document.getElementById('late').value = late
//   document.getElementById('oded2').value = otherDeduction

//   document.getElementById('tran2').value = zero
//   document.getElementById('falw2').value = zero
//   document.getElementById('oded2').value = zero
//   document.getElementById('dbns2').value = zero
//   document.getElementById('atbns2').value =zero
//   document.getElementById('lrep').value = zero
//   document.getElementById('lref2').value =zero
//   document.getElementById('spbonus2').value = zero
//   document.getElementById('late').value = zero
//   late = zero
//   loan = zero
//   otherDeduction = zero
//   var medf
//   var education = document.getElementById('edu').value

//   var IET = (parseInt(edf) + parseInt(education)) / 13
//   medf = Math.round(IET)
  
  
//   // PAYE
//   var basic
//   var gross
//   var nsf
//   var csg
//   var tgross
//   var paye

//   if(document.getElementById('bsal').value){
//     basic = document.getElementById('bsal').value
//   }
//   // alert( basic)
//   // alert( arr)
//   // alert(overseas)
//   // alert(travel)
//   // alert(otherAllow)
//   // alert(car)
//   // Include ALl Value
//   tgross = parseInt(basic) + parseInt(arr) + parseInt(overseas) + parseInt(travel) + parseInt(otherAllow) + parseInt(car)
//   // alert(tgross)
//   document.getElementById('pay').value = tgross
//   // All value with Tax
//   var netgross = parseInt(basic) + parseInt(arr) + parseInt(tax) + parseInt(travel) + parseInt(otherAllow) + parseInt(car) 
//   // alert(netgross)
//   // 329531
//   if(overseas > 0){  
//     gross = netgross
//   }
//   else{    
//     gross = tgross
//   }
  
//   var total = parseInt(gross) - parseInt(medf)
//   if(basic > 50000){
//     paye = total * 0.15
//     document.getElementById('paye').value = Math.round(paye)

//     csg = basic * 0.03
//     document.getElementById('nps').value = Math.round(csg)
//   }
//   else{
//     paye = total * 0.1
//     document.getElementById('paye').value = Math.round(paye)

//     csg = basic * 0.015
//     document.getElementById('nps').value = Math.round(csg)
//   } 
//   var slevy
//   nsf = basic * 0.01
//   if(nsf > 213){
//     nsf = 213
//     document.getElementById('nsf').value = 213
//   }
//   else{
//     document.getElementById('nsf').value = Math.round(nsf)
//   }
//   var limit =Math.round(tgross * 13)
//   if(limit > 3000000){
//     var levy = gross - medf - (3000000/13)
//     var slevy1 = levy * 0.25

//     var slevy2 = gross * 0.10
    
//     if(slevy1 > slevy2){
//       slevy = slevy2
//       document.getElementById('levy').value = Math.round(slevy)
//     }
//     else{
//       slevy = slevy1
//       document.getElementById('levy').value = Math.round(slevy)
//     }
//   }
//   else{
//     slevy = 0
//     document.getElementById('levy').value = slevy
//   }
  
  
//   var deduction = Math.round(loan) + Math.round(paye)+ Math.round(late)+ Math.round(otherDeduction)+ Math.round(csg)+ Math.round(nsf)
//   document.getElementById('ded').value = deduction
//   // alert(tgross) 
//   // 348140
//   var netpay
   
  
//   netpay = tgross - deduction - slevy
//   // alert(netgross)
//   // 329513
//   document.getElementById('npay').value = Math.round(netpay)
// }