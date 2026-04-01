//getting form
const order_form=document.getElementById('orderForm')
const rs_box=document.getElementById('result')
const btn=document.getElementById('submitBtn')
//handling form submit
order_form.addEventListener('submit',async(evt)=>{
 evt.preventDefault()
 btn.innerText='Sending...'
 //reading inputs
 const sym=document.getElementById('symbol').value
 const side=document.getElementById('side').value
 const kind=document.getElementById('type').value
 const qty=document.getElementById('qty').value
 const price=document.getElementById('price').value
 const stop=document.getElementById('stop').value
 const payload={
  symbol:sym,
  side:side,
  type:kind,
  qty:qty,
  price:price,
  stop_price:stop
 }
 try{
  rs_box.classList.add('hidden')
  //sending data to server
  const r=await fetch('/api/order',{
   method:'POST',
   headers:{'Content-Type':'application/json'},
   body:JSON.stringify(payload)
  })
  const j=await r.json()
  //showing result
  rs_box.classList.remove('hidden')
  if(j.success){
   rs_box.className='success-box'
   const dt=j.data
   rs_box.innerHTML=`Order Placed Successfully!<br><br><b>Order ID:</b> ${dt.orderId}<br><b>Symbol:</b> ${dt.symbol}<br><b>Status:</b> ${dt.status}<br><b>Executed Qty:</b> ${dt.executedQty||'0'}<br><b>Avg Price:</b> ${dt.avgPrice||'0'}`
  }else{
   rs_box.className='error-box'
   rs_box.innerHTML='Failed: '+j.error
  }
 }catch(err){
  rs_box.classList.remove('hidden')
  rs_box.className='error-box'
  rs_box.innerHTML='Network Error'
 }
 btn.innerText='Submit Order'
})
//showing extra fields
const t_select=document.getElementById('type')
const p_box=document.getElementById('price-group')
const sp_box=document.getElementById('stop-group')
//checking type change
t_select.addEventListener('change',(e)=>{
 const v=e.target.value
 if(v==='MARKET'||v==='TWAP'){
  p_box.style.display='none'
  sp_box.style.display='none'
 }else if(v==='LIMIT'||v==='GRID'){
  p_box.style.display='block'
  sp_box.style.display='none'
 }else{
  p_box.style.display='block'
  sp_box.style.display='block'
 }
})
t_select.dispatchEvent(new Event('change'))
