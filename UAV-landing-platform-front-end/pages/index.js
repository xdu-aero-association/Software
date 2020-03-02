import React, { Fragment } from 'react';
import { 
    ChartCard, 
    Field, 
    MiniArea, 
    MiniBar, 
    MiniProgress, 
    Pie,
    WaterWave, 
    Gauge,
    TimelineChart,
    Bar,
} from 'ant-design-pro/lib/Charts';
import Trend from 'ant-design-pro/lib/Trend';
import NumberInfo from 'ant-design-pro/lib/NumberInfo';
import { 
    Row, 
    Col, 
    Icon, 
    Tooltip,
    Statistic,
    Card,
} from 'antd';
import numeral from 'numeral';
import moment from 'moment';
import 'ant-design-pro/dist/ant-design-pro.css';

const visitData = [];
const beginDay = new Date().getTime();
for (let i = 0; i < 20; i += 1) {
  visitData.push({
    x: moment(new Date(beginDay + 1000 * 60 * 60 * 24 * i)).format('YYYY-MM-DD'),
    y: Math.floor(Math.random() * 100) + 10,
  });
}


const chartData = [];
for (let i = 0; i < 20; i += 1) {
  chartData.push({
    x: new Date().getTime() + 1000 * 60 * 30 * i,
    y1: Math.floor(Math.random() * 100) + 1000,
  });
}

const salesData = [];
for (let i = 0; i < 12; i += 1) {
  salesData.push({
    x: `${i + 1}月`,
    y: Math.floor(Math.random() * 1000) + 200,
  });
}

export default class extends React.Component {

    render = () => <Fragment>
        <Row>
            <Col span={6}>
                <Card>
                    <Statistic title="无人机编号" value={1234567}/>
                </Card>
            </Col>

            <Col span={6}>
                <Card height={120} style={{textAlign: 'center',}}>
                    <Statistic title="当前高度" suffix={'m'} value={16.87} precision={2}/>
                </Card>
            </Col>

            <Col span={6}>
                <Card>
                    <Statistic title="当前温度" suffix={'℃'} value={23.6} precision={1}/>
                </Card>
            </Col>

            <Col span={6}>
                <Card>
                    <Statistic title="待定数据" value={0}/>
                </Card>
            </Col>

            <Col span={4}>
                <Card>
                    <WaterWave height={120} title="当前空气湿度" percent={34}/>
                </Card>
            </Col>

            <Col span={20}>
                <ChartCard title="历史数据">
                    <MiniArea line height={112} data={visitData} />
                </ChartCard>
            </Col>
        </Row>

        

        <ChartCard title="">
            <Bar height={200} title="历史数据" data={salesData} />
        </ChartCard>
    </Fragment>;
}
