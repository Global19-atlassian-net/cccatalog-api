"""Add reporting tables

Revision ID: beb6d39f2dfd
Revises: 0cd416f5a7d2
Create Date: 2020-10-01 19:43:24.689567

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'beb6d39f2dfd'
down_revision = '0cd416f5a7d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attribution_referer_report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('domain', sa.String(), nullable=True),
    sa.Column('hits', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_attribution_referer_report_domain'), 'attribution_referer_report', ['domain'], unique=False)
    op.create_index(op.f('ix_attribution_referer_report_end_time'), 'attribution_referer_report', ['end_time'], unique=False)
    op.create_index(op.f('ix_attribution_referer_report_hits'), 'attribution_referer_report', ['hits'], unique=False)
    op.create_index(op.f('ix_attribution_referer_report_start_time'), 'attribution_referer_report', ['start_time'], unique=False)
    op.create_table('source_report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('source_id', sa.String(), nullable=True),
    sa.Column('result_clicks', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_source_report_end_time'), 'source_report', ['end_time'], unique=False)
    op.create_index(op.f('ix_source_report_result_clicks'), 'source_report', ['result_clicks'], unique=False)
    op.create_index(op.f('ix_source_report_source_id'), 'source_report', ['source_id'], unique=False)
    op.create_index(op.f('ix_source_report_start_time'), 'source_report', ['start_time'], unique=False)
    op.create_table('top_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('result_uuid', postgresql.UUID(), nullable=True),
    sa.Column('hits', sa.Integer(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_top_results_end_time'), 'top_results', ['end_time'], unique=False)
    op.create_index(op.f('ix_top_results_hits'), 'top_results', ['hits'], unique=False)
    op.create_index(op.f('ix_top_results_result_uuid'), 'top_results', ['result_uuid'], unique=False)
    op.create_index(op.f('ix_top_results_source'), 'top_results', ['source'], unique=False)
    op.create_index(op.f('ix_top_results_start_time'), 'top_results', ['start_time'], unique=False)
    op.create_index(op.f('ix_top_results_title'), 'top_results', ['title'], unique=False)
    op.create_table('top_searches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('term', sa.String(), nullable=True),
    sa.Column('hits', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_top_searches_end_time'), 'top_searches', ['end_time'], unique=False)
    op.create_index(op.f('ix_top_searches_hits'), 'top_searches', ['hits'], unique=False)
    op.create_index(op.f('ix_top_searches_start_time'), 'top_searches', ['start_time'], unique=False)
    op.create_index(op.f('ix_top_searches_term'), 'top_searches', ['term'], unique=False)
    op.create_table('usage_reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('results_clicked', sa.Integer(), nullable=True),
    sa.Column('attribution_buttonclicks', sa.Integer(), nullable=True),
    sa.Column('survey_responses', sa.Integer(), nullable=True),
    sa.Column('source_clicked', sa.Integer(), nullable=True),
    sa.Column('creator_clicked', sa.Integer(), nullable=True),
    sa.Column('shared_social', sa.Integer(), nullable=True),
    sa.Column('sessions', sa.Integer(), nullable=True),
    sa.Column('searches', sa.Integer(), nullable=True),
    sa.Column('attribution_referer_hits', sa.Integer(), nullable=True),
    sa.Column('avg_rating', sa.Float(), nullable=True),
    sa.Column('avg_searches_per_session', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usage_reports_end_time'), 'usage_reports', ['end_time'], unique=False)
    op.create_index(op.f('ix_usage_reports_start_time'), 'usage_reports', ['start_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_usage_reports_start_time'), table_name='usage_reports')
    op.drop_index(op.f('ix_usage_reports_end_time'), table_name='usage_reports')
    op.drop_table('usage_reports')
    op.drop_index(op.f('ix_top_searches_term'), table_name='top_searches')
    op.drop_index(op.f('ix_top_searches_start_time'), table_name='top_searches')
    op.drop_index(op.f('ix_top_searches_hits'), table_name='top_searches')
    op.drop_index(op.f('ix_top_searches_end_time'), table_name='top_searches')
    op.drop_table('top_searches')
    op.drop_index(op.f('ix_top_results_title'), table_name='top_results')
    op.drop_index(op.f('ix_top_results_start_time'), table_name='top_results')
    op.drop_index(op.f('ix_top_results_source'), table_name='top_results')
    op.drop_index(op.f('ix_top_results_result_uuid'), table_name='top_results')
    op.drop_index(op.f('ix_top_results_hits'), table_name='top_results')
    op.drop_index(op.f('ix_top_results_end_time'), table_name='top_results')
    op.drop_table('top_results')
    op.drop_index(op.f('ix_source_report_start_time'), table_name='source_report')
    op.drop_index(op.f('ix_source_report_source_id'), table_name='source_report')
    op.drop_index(op.f('ix_source_report_result_clicks'), table_name='source_report')
    op.drop_index(op.f('ix_source_report_end_time'), table_name='source_report')
    op.drop_table('source_report')
    op.drop_index(op.f('ix_attribution_referer_report_start_time'), table_name='attribution_referer_report')
    op.drop_index(op.f('ix_attribution_referer_report_hits'), table_name='attribution_referer_report')
    op.drop_index(op.f('ix_attribution_referer_report_end_time'), table_name='attribution_referer_report')
    op.drop_index(op.f('ix_attribution_referer_report_domain'), table_name='attribution_referer_report')
    op.drop_table('attribution_referer_report')
    # ### end Alembic commands ###