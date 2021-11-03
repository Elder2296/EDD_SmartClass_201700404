import React,{Component} from 'react'
import {Icon, Menu,Segment} from 'semantic-ui-react'
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom'

export default class MenuExampleInvertedSecondary extends Component {
    state = {activeItem: 'Inicio'}
    

    handleItemClick = (e,{name})=> this.setState({activeItem:name})
    render(){
        const { activeItem } = this.state

        return(
            <>
            <Segment inverted>
                <Menu  inverted pointing secondary class ="ui large menu">
                    <Menu.Item
                        name = 'Inicio'
                        active = {activeItem ==='Inicio'}
                        onClick = {this.handleItemClick}
                        as = {Link} to={'/Admin/'}
                    />
                    <Menu.Item
                        name = 'Reportes'
                        active = {activeItem ==='Reportes'}
                        onClick = {this.handleItemClick}
                        as = {Link} to={'/Admin/Reportes'}
                    />
                    
                    
                    <div class="right item">
                       
                        <Link ><a class="ui inverted button"><i class=" mind sign-out icon"></i>Log out</a></Link>
                        
                    
                    </div>
                    
                    
                </Menu>
                
            </Segment>
            </>
        )
            
        
    }
}
