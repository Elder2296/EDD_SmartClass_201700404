import React,{Component} from 'react'
import { Menu,Segment } from 'semantic-ui-react'
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom'
export default class MenuExampleInvertedSecondary extends Component{

    state = {activeItem: 'Home'}

    handleItemClick = (e,{name})=> this.setState({activeItem:name})
    render(){
        const { activeItem } = this.state

        return(
            <>
            <Segment inverted>
                <Menu  inverted pointing secondary class ="ui large menu">
                    <Menu.Item
                        name = 'Home'
                        active = {activeItem ==='Home'}
                        onClick = {this.handleItemClick}
                        as = {Link} to={'/'}
                    />
                    <div class="right item">
                        <Link to={'/Login'}><a class="ui inverted button">Sing in</a></Link>
                        <Link to={'/Register'}><a class="ui inverted button">Sing up</a></Link>
                        
                    
                    </div>
                </Menu>
                
            </Segment>
            </>
        )
            
        
    }
}
