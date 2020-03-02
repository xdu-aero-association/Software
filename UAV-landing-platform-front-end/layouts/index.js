import { Layout, Menu, Icon } from 'antd';
import Link from 'umi/link'

export default ({ children }) => {

    const { Header, Footer, Sider, Content } = Layout;

    return (
    <Layout>
        <Sider width={256} style={{ minHeight: '100vh' }}>
            <div style={{ height: '32px', background: 'rgba(255,255,255,.2)', margin: '16px'}}/>
            
            <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
                <Menu.Item key="1">
                    <Link to="/">
                        <Icon type="pie-chart" />
                        <span>总览</span>
                    </Link>                    
                </Menu.Item>

                <Menu.Item key="2">
                    <Icon type="pie-chart" />
                    <span>待定</span>
                </Menu.Item>            
            </Menu>
        </Sider>
        
        <Layout>
            <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>Header</Header>
            
            <Content style={{ margin: '24px 16px 0', }}>
                {children}
            </Content>
          
            <Footer style={{ textAlign: 'center' }}> Footer </Footer>
        </Layout>
    </Layout>);
};