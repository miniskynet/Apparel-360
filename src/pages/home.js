import React from 'react';

class Home extends React.Component{
    render(){
    return(
        <div>
            <div class="box">
		<a href="assest/Login.html"><button id="login_button" class="indexbtn">Login</button></a>
		<a href="assest/Signup.html"><button id="signup_button" class="indexbtn2">Signup</button></a>
   </div>	
  <div>
    <div class="description">
      <h1>Apparel 360</h1>
      <p><b>Apparel 360 is an augmented reality<br/> based web-application
      which helps<br/> customers preview tailor-made clothes<br/> cast onto a 3D model</b></p>
	  <br/>
      <a href="assest/HomePage.html"><button class="welcomepage_button">Proceed as guest</button></a>
    </div>
	<div class="index_images">
		<div class="index_img">
			<img src = "assest/img/Black-shirt.png" width="150" height="165" class="round_images" />
		</div>
		<div class="index_img1">
			<img src = "assest/img/Black-shirt1.png" width="150" height="165" class="round_images" />
		</div>
		<div class="index_img2">
			<img src = "assest/img/Red-Shirt.jpg" width="330" height="310" class="round_images" />
		</div>
	</div>
		<div class="index_img3">
			<img src = "assest/img/Black-shirt2.png" width="330" height="310" class="round_images" />
		</div>
		<div class="index_img4">
			<img src = "assest/img/Grey-shirt.png" width="150" height="165" class="round_images" />
		</div>	
		<div class="index_img5">
			<img src = "assest/img/White-shirt.png" width="150" height="165" class="round_images" />
		</div>	
        </div>
        </div>
    );
    }
}

export default Home;