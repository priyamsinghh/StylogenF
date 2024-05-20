import React from "react";
import "./EnterPortal.scss"
import { Link } from 'react-router-dom';
import logo from "../../assets/1.svg";
const EnterPortal = () => {
    return (
        <div className="enterportal">
            <div className="background-overlay"></div>
            <div className="background-image"></div>
            <div className="logo">
                <object type="image/svg+xml" data={logo} width="130" height="130">
                    Your browser does not support SVG.
                </object>
            </div>
            <div className="container">
                {/* <h1>Elevate your style with our <div className="tex">AI-powered Conversational Outfit Generator!</div>  */}
                {/* Discover unique outfit ideas effortlessly, curated by generative AI.</h1> */}
                <h1>Revolutionize Your Wardrobe Using<div className="tex">Innovative AI-Driven Outfit Suggestions!</div>Unleash Your Style Potential with AI-Powered Fashion</h1>
                <div className="buttons">
                    <Link to="login" className="login">Login</Link>
                    <Link to="register" className="signup">Sign Up</Link>
                </div>
            </div>
        </div>
    )
}

export default EnterPortal;