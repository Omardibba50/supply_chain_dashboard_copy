import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import openpyxl
import io
from typing import Dict, List
import io

class AdvancedSupplyChainAnalyzer:
    def __init__(self):
        self.suppliers_data = None
        self.performance_data = None
        self.cost_analysis = None
        self.colors = {
            'primary': '#60a5fa',      # Bright blue
            'secondary': '#c084fc',     # Purple
            'accent': '#7dd3fc',       # Light blue
            'success': '#4ade80',      # Green
            'warning': '#fbbf24',      # Yellow
            'danger': '#f87171',       # Red
            'background': '#0f172a',   # Dark navy
            'surface': '#1e293b',      # Lighter navy
            'text': '#f8fafc',        # White
            'muted': '#94a3b8',       # Gray
            'border': '#334155',      # Border color
            'grid': 'rgba(148, 163, 184, 0.1)',  # Grid lines
            'grid_strong': 'rgba(148, 163, 184, 0.2)',  # Stronger grid
            'highlight': '#38bdf8',    # Highlight blue
            'chart_colors': ['#60a5fa', '#4ade80', '#fbbf24', '#f87171', '#c084fc', '#38bdf8']  # Chart series colors
        }

    def generate_realistic_data(self):
        """Generate comprehensive realistic supplier ecosystem data"""
        np.random.seed(42)
        
        # Supplier portfolio
        suppliers = {
            'Supplier_ID': [f'SUP{str(i).zfill(3)}' for i in range(1, 26)],
            'Supplier_Name': [
                'TechNova Electronics', 'GlobalMech Industries', 'PrecisionCast Ltd', 'RapidLogistics GmbH',
                'EcoSustain Materials', 'QualityPrime Manufacturing', 'InnovateTech Solutions', 'MetalWorks International',
                'ChemSupply Corp', 'ComponentsPlus Ltd', 'FastTrack Logistics', 'ReliableParts Co',
                'AdvancedMaterials Inc', 'SmartComponents SA', 'FlexiManufacturing', 'TechAssembly Group',
                'PremiumParts Ltd', 'IndustrialSupply Co', 'NextGen Components', 'ProManufacturing Solutions',
                'EliteSuppliers Inc', 'MegaCorp Industries', 'SpecialtyMaterials Ltd', 'TechVision Components',
                'GlobalTech Partners'
            ],
            'Country': [
                'Germany', 'China', 'USA', 'Germany', 'Netherlands', 'Japan', 'South Korea', 'Italy',
                'India', 'UK', 'Mexico', 'Turkey', 'Canada', 'France', 'Brazil', 'Vietnam',
                'Poland', 'Czech Republic', 'Malaysia', 'Thailand', 'Taiwan', 'Singapore', 'Spain', 'Belgium', 'Switzerland'
            ],
            'Category': [
                'Electronics', 'Mechanical Parts', 'Castings & Forgings', 'Logistics Services', 'Raw Materials',
                'Assemblies', 'Electronics', 'Metal Components', 'Chemical Supplies', 'Electronic Components',
                'Logistics Services', 'Mechanical Parts', 'Advanced Materials', 'Smart Components', 'Manufacturing Services',
                'Assembly Services', 'Precision Parts', 'Industrial Supplies', 'High-Tech Components', 'Manufacturing Solutions',
                'Premium Components', 'Heavy Industry', 'Specialty Materials', 'Tech Components', 'Technology Solutions'
            ],
            'Supplier_Tier': ['Tier 1', 'Tier 2', 'Tier 1', 'Tier 3', 'Tier 2', 'Tier 1', 'Tier 1', 'Tier 2',
                              'Tier 2', 'Tier 2', 'Tier 3', 'Tier 2', 'Tier 1', 'Tier 1', 'Tier 2', 'Tier 2',
                              'Tier 1', 'Tier 2', 'Tier 1', 'Tier 1', 'Tier 1', 'Tier 2', 'Tier 2', 'Tier 1', 'Tier 1'],
            'Contract_Start': pd.to_datetime([
                '2020-01-15', '2019-06-01', '2021-03-10', '2022-11-20', '2020-05-01', '2019-09-15', '2021-02-01',
                '2020-12-01', '2021-04-15', '2019-08-01', '2022-01-10', '2020-07-15', '2021-06-01', '2019-11-20',
                '2022-03-15', '2020-09-01', '2021-05-20', '2020-02-28', '2019-12-15', '2021-08-10', '2020-10-05',
                '2019-04-12', '2022-02-28', '2021-01-18', '2020-06-22'
            ]),
            'Annual_Volume_USD': [
                5500000, 3200000, 4800000, 1200000, 6200000, 4500000, 3800000, 2900000, 2100000, 3400000,
                800000, 2800000, 5100000, 4200000, 1900000, 2500000, 4700000, 1800000, 5800000, 4100000,
                6800000, 7200000, 2300000, 3900000, 5600000
            ],
            'Certification_Level': ['ISO9001+AS9100', 'ISO9001', 'ISO9001+ISO14001', 'ISO9001', 'ISO14001+OHSAS18001',
                                   'ISO9001+AS9100', 'ISO9001+ISO27001', 'ISO9001+ISO14001', 'ISO9001', 'ISO9001',
                                   'None', 'ISO9001', 'ISO9001+AS9100+ISO14001', 'ISO9001+ISO27001', 'ISO9001',
                                   'ISO9001', 'ISO9001+AS9100', 'ISO9001', 'ISO9001+AS9100+ISO14001', 'ISO9001+AS9100',
                                   'ISO9001+AS9100', 'ISO9001+ISO14001', 'ISO9001+ISO14001', 'ISO9001+AS9100', 'ISO9001+AS9100+ISO27001']
        }
        
        self.suppliers_data = pd.DataFrame(suppliers)
        
        # Generate 24 months of performance data
        performance_records = []
        for supplier_id in self.suppliers_data['Supplier_ID']:
            supplier_info = self.suppliers_data[self.suppliers_data['Supplier_ID'] == supplier_id].iloc[0]
            tier_multiplier = {'Tier 1': 1.0, 'Tier 2': 0.9, 'Tier 3': 0.8}[supplier_info['Supplier_Tier']]
            country_reliability = self._get_country_reliability(supplier_info['Country'])
            
            base_quality = min(98, 75 + (tier_multiplier * 20) + (country_reliability * 5))
            base_delivery = min(98, 70 + (tier_multiplier * 25) + (country_reliability * 5))
            base_cost_competitiveness = 0.7 + (0.6 * np.random.random())
            
            for month_offset in range(24):
                date_record = datetime.now() - timedelta(days=30 * month_offset)
                seasonal_factor = 1 + 0.1 * np.sin(2 * np.pi * month_offset / 12)
                trend_factor = 1 + (month_offset * 0.002)
                
                quality_score = max(60, min(100, base_quality + np.random.normal(0, 4) * seasonal_factor))
                delivery_rate = max(60, min(100, base_delivery + np.random.normal(0, 6) * seasonal_factor))
                base_volume = supplier_info['Annual_Volume_USD'] / 12
                volume_variation = np.random.normal(1, 0.15) * seasonal_factor
                monthly_volume = max(0, base_volume * volume_variation)
                
                units_ordered = int(monthly_volume / np.random.uniform(20, 80))
                units_delivered = int(units_ordered * (delivery_rate / 100))
                
                record = {
                    'Supplier_ID': supplier_id,
                    'Month': date_record.strftime('%Y-%m'),
                    'Date': date_record,
                    'Units_Ordered': units_ordered,
                    'Units_Delivered': units_delivered,
                    'On_Time_Delivery_Rate': delivery_rate,
                    'Quality_Score': quality_score,
                    'Unit_Cost_USD': np.random.uniform(25, 120) * base_cost_competitiveness,
                    'Lead_Time_Days': max(1, int(np.random.normal(12, 5))),
                    'Defect_Rate_PPM': max(0, np.random.exponential(150)),
                    'First_Pass_Yield': max(80, min(100, quality_score + np.random.normal(0, 3))),
                    'Communication_Response_Hours': max(0.5, np.random.exponential(4)),
                    'Invoice_Accuracy_Rate': max(90, min(100, 96 + np.random.normal(0, 2))),
                    'Sustainability_Score': min(10, max(1, 5 + country_reliability + np.random.normal(0, 1))),
                    'Innovation_Score': min(10, max(1, tier_multiplier * 7 + np.random.normal(0, 1.5))),
                    'Financial_Stability_Score': min(10, max(1, 6 + country_reliability + np.random.normal(0, 1))),
                    'Capacity_Utilization': max(40, min(100, 75 + np.random.normal(0, 15)))
                }
                
                record['Total_Cost_USD'] = record['Units_Delivered'] * record['Unit_Cost_USD']
                record['OTIF_Rate'] = record['On_Time_Delivery_Rate'] * (record['Quality_Score'] / 100)
                
                performance_records.append(record)
        
        self.performance_data = pd.DataFrame(performance_records)

    def _get_country_reliability(self, country: str) -> float:
        """Get reliability score for a country"""
        tier_1_countries = {'Germany', 'Japan', 'USA', 'Switzerland', 'Netherlands'}
        tier_2_countries = {'UK', 'France', 'Italy', 'South Korea', 'Taiwan', 'Singapore'}
        
        if country in tier_1_countries:
            return 1.0
        elif country in tier_2_countries:
            return 0.9
        return 0.8
    
    def calculate_advanced_metrics(self):
        """Calculate advanced performance metrics"""
        if self.suppliers_data is None:
            self.generate_realistic_data()
            
        # Calculate performance metrics for each supplier
        performance_metrics = []
        for _, supplier in self.suppliers_data.iterrows():
            # Base performance calculations
            tier_multiplier = {'Tier 1': 1.0, 'Tier 2': 0.9, 'Tier 3': 0.8}[supplier['Supplier_Tier']]
            country_reliability = self._get_country_reliability(supplier['Country'])
            
            # Calculate performance scores
            quality_score = min(98, 75 + (tier_multiplier * 20) + (country_reliability * 5))
            delivery_score = min(98, 70 + (tier_multiplier * 25) + (country_reliability * 5))
            risk_score = max(20, 100 - quality_score)  # Inverse of quality score
            
            performance_metrics.append({
                'Supplier_ID': supplier['Supplier_ID'],
                'Overall_Performance_Score': round((quality_score + delivery_score) / 2, 1),
                'Supply_Risk_Score': round(risk_score, 1),
                'Quality_Score': round(quality_score, 1),
                'Delivery_Score': round(delivery_score, 1),
                'Year': pd.Timestamp.now().year
            })
            
        self.performance_data = pd.DataFrame(performance_metrics)
        
    def get_supply_chain_data(self) -> pd.DataFrame:
        """Get combined supply chain data"""
        if self.performance_data is None:
            self.calculate_advanced_metrics()
        
        df = pd.merge(
            self.suppliers_data,
            self.performance_data,
            on='Supplier_ID',
            how='left'
        )
        
        # Rename Total_Cost_USD to Total_Volume_USD for consistency
        if 'Total_Cost_USD' in df.columns:
            df = df.rename(columns={'Total_Cost_USD': 'Total_Volume_USD'})
            
        return df

    def _calculate_trend(self, series):
        """Calculate trend direction (-1: declining, 0: stable, 1: improving)"""
        if len(series) < 2:
            return 0
        recent_avg = series.head(6).mean()
        older_avg = series.tail(6).mean()
        return 1 if recent_avg > older_avg * 1.05 else -1 if recent_avg < older_avg * 0.95 else 0

    def _calculate_cost_competitiveness(self, unit_cost):
        """Calculate cost competitiveness score"""
        if self.performance_data is None:
            return 50
        all_costs = self.performance_data['Unit_Cost_USD']
        percentile = 100 - (unit_cost / all_costs.max() * 100)
        return max(0, min(100, percentile))

    def _calculate_supply_risk(self, country, delivery_consistency, financial_stability, volume):
        """Calculate supply risk score"""
        country_risk = (1 - self._get_country_reliability(country)) * 40
        delivery_risk = (100 - delivery_consistency) * 0.3
        financial_risk = (10 - financial_stability) * 5
        concentration_risk = min(20, volume / 1000000 * 2)
        return min(100, max(0, country_risk + delivery_risk + financial_risk + concentration_risk))

    def _classify_performance(self, score):
        """Classify supplier performance"""
        if score >= 85:
            return 'Excellent'
        elif score >= 75:
            return 'Good'
        elif score >= 65:
            return 'Acceptable'
        else:
            return 'Needs Improvement'

    def create_modern_dashboard(self, filtered_data=None):
        """Create a modern, simplified supply chain dashboard"""
        if filtered_data is None:
            filtered_data = self.cost_analysis
        
        fig = make_subplots(
            rows=2, cols=3,
            subplot_titles=(
                '<b>Performance vs Risk Matrix</b>', '<b>Cost Competitiveness Analysis</b>', '<b>Quality Performance</b>',
                '<b>Delivery Excellence</b>', '<b>Volume Distribution</b>', '<b>Strategic Value Assessment</b>'
            ),
            specs=[
                [{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}],
                [{"type": "scatter"}, {"type": "bar"}, {"type": "scatter"}]
            ],
            vertical_spacing=0.35,     # Further increased vertical spacing for better separation
            horizontal_spacing=0.2,    # Further increased horizontal spacing
            column_widths=[0.32, 0.32, 0.32],  # Equal widths with slight padding
            row_heights=[0.48, 0.48]  # Slightly adjusted for better balance
        )

        # 1. Performance vs Risk (Bubble Chart)
        fig.add_trace(
            go.Scatter(
                x=filtered_data['Overall_Performance_Score'],
                y=filtered_data['Supply_Risk_Score'],
                mode='markers',  # Removed text to prevent overlapping
                text=filtered_data['Supplier_Name'].str[:10],
                marker=dict(
                    size=filtered_data['Total_Volume_USD']/250000,  # Reduced bubble size
                    color=filtered_data['Strategic_Value_Score'],
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(
                        title="Strategic Value",
                        x=0.35,
                        len=0.3,
                        thickness=10,
                        tickfont={'size': 8}
                    )
                ),
                hovertemplate='<b>%{text}</b><br>Performance: %{x:.1f}%<br>Risk: %{y:.1f}%<br>Volume: $%{marker.size:,.0f}M<extra></extra>',
                name='Suppliers'
            ),
            row=1, col=1
        )

        # 2. Cost Competitiveness
        fig.add_trace(
            go.Scatter(
                x=filtered_data['Avg_Unit_Cost'],
                y=filtered_data['Cost_Competitiveness_Score'],
                mode='markers',
                marker=dict(size=12, color=filtered_data['Quality_Excellence_Score'], colorscale='RdYlGn'),
                text=filtered_data['Supplier_Name'],
                hovertemplate='<b>%{text}</b><br>Unit Cost: $%{x:.2f}<br>Competitiveness: %{y:.1f}%<extra></extra>',
                name='Cost'
            ),
            row=1, col=2
        )

        # 3. Quality Trends
        fig.add_trace(
            go.Scatter(
                x=filtered_data['Avg_Quality_Score'],
                y=filtered_data['Avg_Defect_Rate_PPM'],
                mode='markers',
                marker=dict(size=10, color=filtered_data['Quality_Trend'], colorscale='RdYlGn'),
                text=filtered_data['Supplier_Name'],
                hovertemplate='<b>%{text}</b><br>Quality: %{x:.1f}%<br>Defects: %{y:.0f} PPM<extra></extra>',
                name='Quality'
            ),
            row=1, col=3
        )

        # 4. Delivery Performance
        fig.add_trace(
            go.Scatter(
                x=filtered_data['Avg_Delivery_Rate'],
                y=filtered_data['Delivery_Consistency'],
                mode='markers',
                marker=dict(size=filtered_data['OTIF_Rate']/3, color=filtered_data['Avg_Lead_Time'], colorscale='RdYlBu_r'),
                text=filtered_data['Supplier_Name'],
                hovertemplate='<b>%{text}</b><br>Delivery: %{x:.1f}%<br>Consistency: %{y:.1f}%<extra></extra>',
                name='Delivery'
            ),
            row=2, col=1
        )

        # 5. Volume Distribution (Horizontal Bar)
        # Sort by volume for better visualization
        volume_data = filtered_data.sort_values('Total_Volume_USD', ascending=True).tail(8)  # Show only top 8
        risk_colors = ['#10B981' if x < 30 else '#F59E0B' if x < 60 else '#F87171' 
                      for x in volume_data['Supply_Risk_Score']]
        fig.add_trace(
            go.Bar(
                y=volume_data['Supplier_Name'].str[:10],
                x=volume_data['Total_Volume_USD']/1000000,
                orientation='h',
                marker_color=risk_colors,
                name='Volume (Risk-coded)',
                hovertemplate='<b>%{y}</b><br>Volume: $%{x:.1f}M<extra></extra>',
                width=0.7  # Adjusted bar width
            ),
            row=2, col=2
        )

        # 6. Strategic Value
        fig.add_trace(
            go.Scatter(
                x=filtered_data['Innovation_Score'],
                y=filtered_data['Sustainability_Score'],
                mode='markers',
                marker=dict(size=filtered_data['Financial_Stability_Score']*2, color=filtered_data['Strategic_Value_Score'], colorscale='Plasma'),
                text=filtered_data['Supplier_Name'],
                hovertemplate='<b>%{text}</b><br>Innovation: %{x:.1f}<br>Sustainability: %{y:.1f}<extra></extra>',
                name='Strategic Value'
            ),
            row=2, col=3
        )

        # Add annotation for top performer
        top_performer = filtered_data.loc[filtered_data['Overall_Performance_Score'].idxmax(), 'Supplier_Name']
        fig.add_annotation(
            x=0.5, y=1.05, xref="paper", yref="paper",
            text=f"Top Performer: {top_performer[:10]}",
            showarrow=False, font=dict(size=16, color=self.colors['success'])
        )

        # Update layout with modern styling and better spacing
        fig.update_layout(
            height=1200,  # Further increased height for better overall spacing
            margin=dict(
                t=160,  # More top margin for title
                l=130,  # More left margin for labels
                r=130,  # More right margin for balance
                b=140   # More bottom margin for legend
            ),  # Optimized margins for better spacing
            title={
                'text': "<b>Supply Chain Performance Dashboard</b>",
                'y': 0.99,  # Moved title slightly up
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': {'size': 28, 'family': 'Inter, sans-serif', 'color': self.colors['text'], 'weight': 'bold'}
            },
            showlegend=True,
            legend={
                'orientation': 'h',
                'yanchor': 'bottom',
                'y': -0.25,  # Moved legend further down to prevent overlap
                'xanchor': 'center',
                'x': 0.5,
                'bgcolor': 'rgba(255, 255, 255, 0.05)',  # More subtle background
                'bordercolor': self.colors['border'],
                'borderwidth': 1,
                'font': {'size': 11, 'color': self.colors['text']},
                'itemsizing': 'constant',  # Consistent legend item sizes
                'itemwidth': 40  # Wider legend items for better readability
            },
            paper_bgcolor=self.colors['background'],
            plot_bgcolor=self.colors['background'],
            font={'family': 'Inter, sans-serif', 'size': 12, 'color': self.colors['text']}
        )

        # Update axes
        axis_updates = [
            (1, 1, "Performance Score (%)", "Risk Score (%)"),
            (1, 2, "Unit Cost ($)", "Cost Competitiveness (%)"),
            (1, 3, "Quality Score (%)", "Defect Rate (PPM)"),
            (2, 1, "Delivery Rate (%)", "Consistency (%)"),
            (2, 2, "Suppliers", "Volume ($M)"),
            (2, 3, "Innovation Score", "Sustainability Score")
        ]
        
        # Update subplot titles with better formatting
        for i in range(len(fig.layout.annotations)):
            fig.layout.annotations[i].update(
                font=dict(
                    size=15,  # Increased font size
                    color=self.colors['text'],
                    family='Inter, sans-serif',
                ),
                y=fig.layout.annotations[i].y + 0.04,  # Move titles up more for better spacing
                borderpad=8  # Add padding around subplot titles
            )

        # Update axes formatting
        for row, col, xlabel, ylabel in axis_updates:
            fig.update_xaxes(
                title_text=f"<b>{xlabel}</b>",
                title_font=dict(size=12, color=self.colors['text']),
                title_standoff=15,  # Increased spacing between title and axis
                tickfont=dict(size=10, color=self.colors['muted']),
                showgrid=True,
                gridwidth=1,
                gridcolor='rgba(255, 255, 255, 0.1)',
                showline=True,
                linewidth=1,
                linecolor=self.colors['border'],
                row=row,
                col=col,
                nticks=6,  # Limit number of ticks
                automargin=True,  # Prevent label overlap
                rangemode='tozero'  # Start axes from 0 when possible
            )
            fig.update_yaxes(
                title_text=f"<b>{ylabel}</b>",
                title_font=dict(size=12, color=self.colors['text']),
                title_standoff=15,  # Increased spacing between title and axis
                tickfont=dict(size=10, color=self.colors['muted']),
                showgrid=True,
                gridwidth=1,
                gridcolor='rgba(255, 255, 255, 0.1)',
                showline=True,
                linewidth=1,
                linecolor=self.colors['border'],
                row=row,
                col=col,
                nticks=6,  # Limit number of ticks
                automargin=True  # Prevent label overlap
            )

        # Apply dark theme styling
        self._apply_dark_theme(fig)

        return fig

    def create_modern_dashboard(self, data: pd.DataFrame) -> go.Figure:
        """Create a modern style performance dashboard"""
        # Create subplots with proper layout
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                'Performance by Category',  # Changed from Performance Trends
                'Category Distribution',
                'Risk vs Performance Matrix',
                'Volume Distribution'
            ),
            specs=[
                [{"type": "scatter"}, {"type": "bar"}],  # Changed pie to bar for better readability
                [{"type": "scatter"}, {"type": "bar"}]
            ],
            vertical_spacing=0.25,
            horizontal_spacing=0.15
        )
        
        # Performance by Category with normalized Y-axis
        performance_data = data.groupby('Category')['Overall_Performance_Score'].mean().sort_values()
        fig.add_trace(
            go.Bar(  # Changed from Scatter to Bar
                x=performance_data.index,
                y=performance_data.values,
                name='Performance',
                marker_color=self._generate_color_palette(len(performance_data)),  # Dynamic colors
                text=performance_data.values.round(1),
                textposition='outside',
            ),
            row=1, col=1
        )
        
        # Category Distribution as Bar Chart
        category_dist = data.groupby('Category').agg({
            'Supplier_Name': 'count',
            'Total_Volume_USD': 'sum'
        }).sort_values('Total_Volume_USD', ascending=True)
        
        # Show top 10 categories and aggregate the rest
        if len(category_dist) > 10:
            others = pd.DataFrame({
                'Supplier_Name': [category_dist.iloc[:len(category_dist)-10]['Supplier_Name'].sum()],
                'Total_Volume_USD': [category_dist.iloc[:len(category_dist)-10]['Total_Volume_USD'].sum()]
            }, index=['Others'])
            category_dist = pd.concat([others, category_dist.iloc[-10:]])
        
        fig.add_trace(
            go.Bar(
                y=category_dist.index,
                x=category_dist['Total_Volume_USD'] / 1e6,  # Convert to millions
                orientation='h',
                marker=dict(
                    color=self._generate_color_palette(len(category_dist)),
                    colorscale='Viridis'
                ),
                name='Volume',
                text=(category_dist['Total_Volume_USD'] / 1e6).round(1).astype(str) + 'M',
                textposition='outside',
            ),
            row=1, col=2
        )
        
        # Risk vs Performance Matrix with normalized bubble sizes
        risk_perf = data.groupby('Category').agg({
            'Supply_Risk_Score': 'mean',
            'Overall_Performance_Score': 'mean',
            'Total_Volume_USD': 'sum'
        }).reset_index()
        
        # Normalize bubble sizes to range 20-60
        min_volume = risk_perf['Total_Volume_USD'].min()
        max_volume = risk_perf['Total_Volume_USD'].max()
        normalized_sizes = ((risk_perf['Total_Volume_USD'] - min_volume) / (max_volume - min_volume) * 40 + 20)
        
        fig.add_trace(
            go.Scatter(
                x=risk_perf['Supply_Risk_Score'],
                y=risk_perf['Overall_Performance_Score'],
                mode='markers',
                text=risk_perf['Category'],
                marker=dict(
                    size=normalized_sizes,
                    color=self._generate_color_palette(len(risk_perf)),
                    line=dict(color='white', width=1)
                ),
                name='Categories',
                hovertemplate=(
                    '<b>%{text}</b><br>' +
                    'Risk Score: %{x:.1f}<br>' +
                    'Performance Score: %{y:.1f}<br>' +
                    'Volume: $%{customdata:.1f}M<extra></extra>'
                ),
                customdata=(risk_perf['Total_Volume_USD'] / 1e6)
            ),
            row=2, col=1
        )
        
        # Volume Distribution with risk-based coloring
        volume_dist = data.groupby('Supplier_Name').agg({
            'Total_Volume_USD': 'sum',
            'Supply_Risk_Score': 'mean'
        }).sort_values('Total_Volume_USD', ascending=True)
        
        # Show only top 15 suppliers
        volume_dist = volume_dist.tail(15)
        
        # Generate colors based on risk score
        risk_colors = [
            '#4ade80' if score < 30 else  # Low risk - green
            '#fbbf24' if score < 60 else  # Medium risk - yellow
            '#f87171'                     # High risk - red
            for score in volume_dist['Supply_Risk_Score']
        ]
        
        fig.add_trace(
            go.Bar(
                y=volume_dist.index.str.slice(0, 20),  # Truncate long names
                x=volume_dist['Total_Volume_USD'] / 1e6,
                orientation='h',
                marker_color=risk_colors,
                name='Volume',
                text=(volume_dist['Total_Volume_USD'] / 1e6).round(1).astype(str) + 'M',
                textposition='outside',
                hovertemplate=(
                    '<b>%{y}</b><br>' +
                    'Volume: $%{x:.1f}M<br>' +
                    'Risk Score: %{customdata:.1f}<extra></extra>'
                ),
                customdata=volume_dist['Supply_Risk_Score']
            ),
            row=2, col=2
        )
        
        # Update axis labels and formatting
        fig.update_xaxes(title_text='Category', row=1, col=1)
        fig.update_yaxes(title_text='Performance Score (%)', row=1, col=1)
        
        fig.update_xaxes(title_text='Volume (Millions USD)', row=1, col=2)
        fig.update_yaxes(title_text='Category', row=1, col=2)
        
        fig.update_xaxes(title_text='Risk Score', row=2, col=1)
        fig.update_yaxes(title_text='Performance Score (%)', row=2, col=1)
        
        fig.update_xaxes(title_text='Volume (Millions USD)', row=2, col=2)
        fig.update_yaxes(title_text='Supplier', row=2, col=2)
        
        # Update layout with improved spacing and accessibility
        fig.update_layout(
            height=900,
            showlegend=True,
            margin=dict(t=100, l=80, r=80, b=80),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.15,
                xanchor="center",
                x=0.5,
                font=dict(color=self.colors['text']),
                bgcolor='rgba(0,0,0,0.1)',
                bordercolor=self.colors['border']
            ),
            title=dict(
                text='Supply Chain Performance Dashboard',
                font=dict(color=self.colors['text'], size=24),
                y=0.98,
                x=0.5,
                xanchor='center',
                yanchor='top'
            ),
            paper_bgcolor=self.colors['background'],
            plot_bgcolor=self.colors['background']
        )
        
        # Apply consistent dark theme styling
        self._apply_dark_theme(fig)
        
        return fig
    
    def create_performance_dashboard(self, data: pd.DataFrame) -> go.Figure:
        """Create a performance overview dashboard"""
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Performance by Category', 'Supplier Distribution'),
            specs=[[{'type': 'bar'}, {'type': 'pie'}]]
        )
        
        # Performance by category
        category_perf = data.groupby('Category')['Overall_Performance_Score'].mean().reset_index()
        fig.add_trace(
            go.Bar(
                x=category_perf['Category'],
                y=category_perf['Overall_Performance_Score'],
                name='Performance Score',
                marker_color=self.colors['primary']
            ),
            row=1, col=1
        )
        
        # Supplier distribution
        supplier_dist = data['Category'].value_counts()
        fig.add_trace(
            go.Pie(
                labels=supplier_dist.index,
                values=supplier_dist.values,
                name='Suppliers',
                marker_colors=[self.colors['primary'], self.colors['success'], 
                             self.colors['warning'], self.colors['accent']]
            ),
            row=1, col=2
        )
        
        fig.update_layout(
            height=400,
            showlegend=False,
            title_text='Supply Chain Performance Overview',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        # Apply dark theme styling
        self._apply_dark_theme(fig)
        
        return fig
    
    def create_risk_matrix(self, data: pd.DataFrame) -> go.Figure:
        """Create a risk assessment matrix"""
        fig = go.Figure()
        
        # Calculate mean values for quadrant lines
        x_mean = 50  # Set fixed mean for better visualization
        y_mean = 50  # Set fixed mean for better visualization
        
        # Add quadrant shapes with custom styling
        quadrants = [
            # High Performance, Low Risk (Good)
            dict(
                type="rect",
                x0=0, x1=x_mean,
                y0=y_mean, y1=100,
                fillcolor=self.colors['success'],
                opacity=0.1,
                line_width=0
            ),
            # High Performance, High Risk (Watch)
            dict(
                type="rect",
                x0=x_mean, x1=100,
                y0=y_mean, y1=100,
                fillcolor=self.colors['warning'],
                opacity=0.1,
                line_width=0
            ),
            # Low Performance, Low Risk (Improve)
            dict(
                type="rect",
                x0=0, x1=x_mean,
                y0=0, y1=y_mean,
                fillcolor=self.colors['warning'],
                opacity=0.1,
                line_width=0
            ),
            # Low Performance, High Risk (Critical)
            dict(
                type="rect",
                x0=x_mean, x1=100,
                y0=0, y1=y_mean,
                fillcolor=self.colors['danger'],
                opacity=0.1,
                line_width=0
            )
        ]
        
        # Add scatter plot with normalized size for better visibility
        max_volume = data['Total_Volume_USD'].max()
        normalized_size = data['Total_Volume_USD'] / max_volume * 50 + 10  # Ensures minimum size of 10
        
        fig.add_trace(go.Scatter(
            x=data['Supply_Risk_Score'],
            y=data['Overall_Performance_Score'],
            mode='markers+text',
            marker=dict(
                size=normalized_size,
                color=data['Total_Volume_USD'],
                colorscale=[
                    [0, self.colors['accent']],
                    [0.5, self.colors['primary']],
                    [1, self.colors['secondary']]
                ],
                showscale=True,
                colorbar=dict(
                    title=dict(
                        text="Volume",
                        font=dict(color=self.colors['text'])
                    ),
                    tickfont=dict(color=self.colors['text'])
                ),
                line=dict(width=1, color=self.colors['border'])
            ),
            text=data['Supplier_Name'],
            textposition="top center",
            textfont=dict(size=10, color=self.colors['text']),
            hovertemplate="<b>%{text}</b><br>" +
                         "Risk Score: %{x:.1f}<br>" +
                         "Performance: %{y:.1f}%<br>" +
                         "Volume: $%{marker.color:,.0f}<br>" +
                         "<extra></extra>"
        ))
        
        # Update layout with quadrants and styling
        fig.update_layout(
            shapes=quadrants,
            title=dict(
                text='Supplier Risk Matrix',
                font=dict(size=20, color=self.colors['text'])
            ),
            xaxis=dict(
                title=dict(
                    text='Risk Score',
                    font=dict(size=14, color=self.colors['text'])
                ),
                range=[0, 100],
                showgrid=True,
                gridcolor=self.colors['grid'],
                zeroline=False,
                tickfont=dict(color=self.colors['text'])
            ),
            yaxis=dict(
                title=dict(
                    text='Performance Score',
                    font=dict(size=14, color=self.colors['text'])
                ),
                range=[0, 100],
                showgrid=True,
                gridcolor=self.colors['grid'],
                zeroline=False,
                tickfont=dict(color=self.colors['text'])
            ),
            height=600,
            showlegend=False,
            paper_bgcolor=self.colors['background'],
            plot_bgcolor=self.colors['background']
        )
        
        # Add quadrant labels
        annotations = [
            dict(x=x_mean/2, y=y_mean + (100-y_mean)/2, text="GOOD",
                 font=dict(size=14, color=self.colors['success'])),
            dict(x=x_mean + (100-x_mean)/2, y=y_mean + (100-y_mean)/2, text="WATCH",
                 font=dict(size=14, color=self.colors['warning'])),
            dict(x=x_mean/2, y=y_mean/2, text="IMPROVE",
                 font=dict(size=14, color=self.colors['warning'])),
            dict(x=x_mean + (100-x_mean)/2, y=y_mean/2, text="CRITICAL",
                 font=dict(size=14, color=self.colors['danger']))
        ]
        
        for annotation in annotations:
            fig.add_annotation(
                x=annotation['x'],
                y=annotation['y'],
                text=annotation['text'],
                font=annotation['font'],
                showarrow=False,
                xanchor='center',
                yanchor='middle'
            )
        
        return fig
    
    def create_volume_chart(self, data: pd.DataFrame) -> go.Figure:
        """Create a volume distribution chart"""
        fig = go.Figure()
        
        # Sort data by volume for better visualization
        data_sorted = data.sort_values('Total_Volume_USD', ascending=True)
        
        fig.add_trace(go.Bar(
            x=data_sorted['Category'],
            y=data_sorted['Total_Volume_USD'] / 1000000,  # Convert to millions
            marker=dict(
                color=data_sorted['Total_Volume_USD'],
                colorscale=[[0, self.colors['accent']], [1, self.colors['primary']]],
                showscale=True,
                colorbar=dict(
                    title=dict(
                        text="Volume",
                        font=dict(color=self.colors['text'])
                    ),
                    ticksuffix="M",
                    tickfont=dict(color=self.colors['text'])
                )
            ),
            hovertemplate="<b>%{x}</b><br>" +
                         "Volume: $%{y:.1f}M<br>" +
                         "<extra></extra>"
        ))
        
        fig.update_layout(
            title=dict(
                text='Volume Distribution by Category',
                font=dict(size=20, color=self.colors['text'])
            ),
            xaxis_title=dict(
                text='Category',
                font=dict(size=14, color=self.colors['text'])
            ),
            yaxis_title=dict(
                text='Volume (Millions USD)',
                font=dict(size=14, color=self.colors['text'])
            ),
            height=500,
            paper_bgcolor=self.colors['background'],
            plot_bgcolor=self.colors['background'],
            bargap=0.2
        )
        
        # Add value annotations
        for i in range(len(data_sorted)):
            fig.add_annotation(
                x=data_sorted['Category'].iloc[i],
                y=data_sorted['Total_Volume_USD'].iloc[i] / 1000000,
                text=f"${data_sorted['Total_Volume_USD'].iloc[i]/1000000:.1f}M",
                showarrow=False,
                font=dict(color=self.colors['text']),
                yshift=10
            )
        
        # Apply dark theme styling
        self._apply_dark_theme(fig)
        
        return fig
        
    def export_report(self) -> bytes:
        """Export dashboard data as Excel report"""
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            self.suppliers_data.to_excel(writer, sheet_name='Supplier Data', index=False)
            
            # Add performance metrics
            metrics = pd.DataFrame({
                'Metric': ['Active Suppliers', 'Total Volume (USD)', 'Performance Score', 'High Risk Suppliers'],
                'Value': [
                    self.get_active_suppliers_count(),
                    self.get_total_volume(),
                    self.get_performance_score(),
                    self.get_high_risk_count()
                ]
            })
            metrics.to_excel(writer, sheet_name='Key Metrics', index=False)
            
        return output.getvalue()
            
    def generate_strategic_insights(self) -> Dict:
        """Generate strategic insights for the dashboard"""
        return {
            'Executive Summary': {
                'Overall Health Score': f"{self.get_performance_score()}%",
                'Risk Level': 'Moderate',
                'Growth Trajectory': 'Positive',
                'Cost Efficiency': 'Above Target'
            },
            'Key Recommendations': [
                {'Area': 'Risk Management', 'Action': 'Implement advanced monitoring for high-risk suppliers'},
                {'Area': 'Performance', 'Action': 'Develop improvement plans for bottom 20% performers'},
                {'Area': 'Cost', 'Action': 'Negotiate volume-based discounts with top suppliers'},
                {'Area': 'Sustainability', 'Action': 'Increase focus on suppliers with green certifications'}
            ]
        }
    
    def get_active_suppliers_count(self) -> int:
        """Return the count of active suppliers"""
        if self.suppliers_data is None:
            self.generate_realistic_data()
        return len(self.suppliers_data)
    
    def get_supplier_growth(self) -> float:
        """Calculate the growth in supplier count"""
        return round(np.random.uniform(5, 15), 1)  # Simulated growth rate
    
    def get_total_volume(self) -> float:
        """Get total volume in USD"""
        if self.suppliers_data is None:
            self.generate_realistic_data()
        return self.suppliers_data['Annual_Volume_USD'].sum()
    
    def get_volume_growth(self) -> float:
        """Calculate volume growth rate"""
        return round(np.random.uniform(8, 20), 1)  # Simulated growth rate
    
    def get_performance_score(self) -> float:
        """Calculate overall performance score"""
        if self.performance_data is None:
            self.calculate_advanced_metrics()
        return round(self.performance_data['Overall_Performance_Score'].mean(), 1)
    
    def get_performance_change(self) -> float:
        """Calculate change in performance score"""
        return round(np.random.uniform(-5, 8), 1)  # Simulated performance change
    
    def get_high_risk_count(self) -> int:
        """Get count of high risk suppliers"""
        if self.performance_data is None:
            self.calculate_advanced_metrics()
        return int(sum(self.performance_data['Supply_Risk_Score'] > 70))
    
    def get_risk_change(self) -> float:
        """Calculate change in high risk count"""
        return round(np.random.uniform(-15, 5), 1)  # Simulated risk change

    def _apply_dark_theme(self, fig):
        """Apply consistent dark theme styling to charts"""
        fig.update_xaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor=self.colors['grid'],
            zeroline=False,
            showline=True,
            linewidth=1,
            linecolor=self.colors['border'],
            tickfont=dict(color=self.colors['text']),
            title_font=dict(color=self.colors['text'])
        )
        
        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor=self.colors['grid'],
            zeroline=False,
            showline=True,
            linewidth=1,
            linecolor=self.colors['border'],
            tickfont=dict(color=self.colors['text']),
            title_font=dict(color=self.colors['text'])
        )
        
        fig.update_layout(
            paper_bgcolor=self.colors['background'],
            plot_bgcolor=self.colors['background'],
            font=dict(color=self.colors['text']),
            title_font=dict(color=self.colors['text']),
            legend=dict(
                font=dict(color=self.colors['text']),
                bgcolor='rgba(0,0,0,0)',
                bordercolor=self.colors['border']
            )
        )
    
    def _generate_color_palette(self, n_colors: int) -> list:
        """Generate a colorblind-friendly palette with the specified number of colors"""
        # Use a colorblind-friendly base palette
        base_colors = [
            '#4ade80',  # Green
            '#60a5fa',  # Blue
            '#f87171',  # Red
            '#fbbf24',  # Yellow
            '#c084fc',  # Purple
            '#34d399',  # Teal
            '#f472b6',  # Pink
            '#fb923c',  # Orange
            '#94a3b8',  # Gray
            '#818cf8'   # Indigo
        ]
        
        if n_colors <= len(base_colors):
            return base_colors[:n_colors]
        
        # If we need more colors, interpolate between existing ones
        import numpy as np
        from colour import Color
        
        colors = []
        step = len(base_colors) / n_colors
        for i in range(n_colors):
            idx = int(i * step)
            c1 = Color(base_colors[idx])
            c2 = Color(base_colors[(idx + 1) % len(base_colors)])
            t = (i * step) % 1
            r = c1.red + t * (c2.red - c1.red)
            g = c1.green + t * (c2.green - c1.green)
            b = c1.blue + t * (c2.blue - c1.blue)
            colors.append(f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}')
        
        return colors