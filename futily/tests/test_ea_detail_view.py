from cms import externals
from cms.apps.pages.middleware import RequestPageManager
from cms.apps.pages.models import Page
from django.contrib.contenttypes.models import ContentType
from django.test import RequestFactory
from django.test import TestCase

from ..apps.leagues.models import League, Leagues
from ..apps.nations.models import Nation, Nations
from ..apps.players.models import Player
from ..apps.views import EaDetailView


class TestNationDetailView(EaDetailView):
    model = Nation


class TestNationEaDetailView(TestCase):  # pylint: disable=too-many-instance-attributes
    def setUp(self):
        self.factory = RequestFactory()

        with externals.watson.context_manager('update_index')():
            content_type = ContentType.objects.get_for_model(Nations)

            self.page = Page.objects.create(
                title='Nations',
                slug='nations',
                content_type=content_type
            )

            self.nations = Nations.objects.create(
                page=self.page
            )

            self.nation_pos = Nation.objects.create(
                page=self.nations,
                ea_id=1,
                name='Nation pos',
                name_abbr='Nation pos',
                slug='nation_pos',
                average_rating=10.0,
                total_players=10,
                total_bronze=10,
                total_silver=10,
                total_gold=10,
                total_inform=10,
                total_special=10
            )

            self.nation_lvl = Nation.objects.create(
                page=self.nations,
                ea_id=2,
                name='Nation lvl',
                name_abbr='Nation lvl',
                slug='nation_lvl',
                average_rating=10.0,
                total_players=10,
                total_bronze=10,
                total_silver=10,
                total_gold=10,
                total_inform=10,
                total_special=10
            )

            self.player_gk = Player.objects.create(
                ea_id=1,
                first_name='John',
                last_name='Doe',
                common_name='John Doe GK',
                nation=self.nation_pos,
                position='GK',
                rating=1,
                card_att_1=1,
                card_att_2=17,
                card_att_3=1,
                card_att_4=17,
                card_att_5=1,
                card_att_6=17
            )

            self.player_rwb = Player.objects.create(
                ea_id=2,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RWB',
                nation=self.nation_pos,
                position='RWB',
                rating=2,
                card_att_1=2,
                card_att_2=16,
                card_att_3=2,
                card_att_4=16,
                card_att_5=2,
                card_att_6=16
            )

            self.player_rb = Player.objects.create(
                ea_id=3,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RB',
                nation=self.nation_pos,
                position='RB',
                rating=3,
                card_att_1=3,
                card_att_2=15,
                card_att_3=3,
                card_att_4=15,
                card_att_5=3,
                card_att_6=15
            )

            self.player_cb = Player.objects.create(
                ea_id=4,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CB',
                nation=self.nation_pos,
                position='CB',
                rating=4,
                card_att_1=4,
                card_att_2=14,
                card_att_3=4,
                card_att_4=14,
                card_att_5=4,
                card_att_6=14
            )

            self.player_lb = Player.objects.create(
                ea_id=5,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LB',
                nation=self.nation_pos,
                position='LB',
                rating=5,
                card_att_1=5,
                card_att_2=13,
                card_att_3=5,
                card_att_4=13,
                card_att_5=5,
                card_att_6=13
            )

            self.player_lwb = Player.objects.create(
                ea_id=6,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LWB',
                nation=self.nation_pos,
                position='LWB',
                rating=6,
                card_att_1=6,
                card_att_2=12,
                card_att_3=6,
                card_att_4=12,
                card_att_5=6,
                card_att_6=12
            )

            self.player_cdm = Player.objects.create(
                ea_id=7,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CDM',
                nation=self.nation_pos,
                position='CDM',
                rating=7,
                card_att_1=7,
                card_att_2=11,
                card_att_3=7,
                card_att_4=11,
                card_att_5=7,
                card_att_6=11
            )

            self.player_cm = Player.objects.create(
                ea_id=8,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CM',
                nation=self.nation_pos,
                position='CM',
                rating=8,
                card_att_1=8,
                card_att_2=10,
                card_att_3=8,
                card_att_4=10,
                card_att_5=8,
                card_att_6=10
            )

            self.player_cam = Player.objects.create(
                ea_id=9,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CAM',
                nation=self.nation_pos,
                position='CAM',
                rating=9,
                card_att_1=9,
                card_att_2=9,
                card_att_3=9,
                card_att_4=9,
                card_att_5=9,
                card_att_6=9
            )

            self.player_rm = Player.objects.create(
                ea_id=10,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RM',
                nation=self.nation_pos,
                position='RM',
                rating=10,
                card_att_1=10,
                card_att_2=8,
                card_att_3=10,
                card_att_4=8,
                card_att_5=10,
                card_att_6=8
            )

            self.player_rw = Player.objects.create(
                ea_id=11,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RW',
                nation=self.nation_pos,
                position='RW',
                rating=11,
                card_att_1=11,
                card_att_2=7,
                card_att_3=11,
                card_att_4=7,
                card_att_5=11,
                card_att_6=7
            )

            self.player_rf = Player.objects.create(
                ea_id=12,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RF',
                nation=self.nation_pos,
                position='RF',
                rating=12,
                card_att_1=12,
                card_att_2=6,
                card_att_3=12,
                card_att_4=6,
                card_att_5=12,
                card_att_6=6
            )

            self.player_lm = Player.objects.create(
                ea_id=13,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LM',
                nation=self.nation_pos,
                position='LM',
                rating=13,
                card_att_1=13,
                card_att_2=5,
                card_att_3=13,
                card_att_4=5,
                card_att_5=13,
                card_att_6=5
            )

            self.player_lw = Player.objects.create(
                ea_id=14,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LW',
                nation=self.nation_pos,
                position='LW',
                rating=14,
                card_att_1=14,
                card_att_2=4,
                card_att_3=14,
                card_att_4=4,
                card_att_5=14,
                card_att_6=4
            )

            self.player_lf = Player.objects.create(
                ea_id=15,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LF',
                nation=self.nation_pos,
                position='LF',
                rating=15,
                card_att_1=15,
                card_att_2=3,
                card_att_3=15,
                card_att_4=3,
                card_att_5=15,
                card_att_6=3
            )

            self.player_cf = Player.objects.create(
                ea_id=16,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CF',
                nation=self.nation_pos,
                position='CF',
                rating=16,
                card_att_1=16,
                card_att_2=2,
                card_att_3=16,
                card_att_4=2,
                card_att_5=16,
                card_att_6=2
            )

            self.player_st = Player.objects.create(
                ea_id=17,
                first_name='John',
                last_name='Doe',
                common_name='John Doe ST',
                nation=self.nation_pos,
                position='ST',
                rating=17,
                card_att_1=17,
                card_att_2=1,
                card_att_3=17,
                card_att_4=1,
                card_att_5=17,
                card_att_6=1
            )

            self.player_totw_gold = Player.objects.create(
                ea_id=1,
                first_name='John',
                last_name='Doe',
                common_name='John Doe TOTW Gold',
                nation=self.nation_lvl,
                color='totw_gold'
            )

            self.player_totw_silver = Player.objects.create(
                ea_id=2,
                first_name='John',
                last_name='Doe',
                common_name='John Doe TOTW Silver',
                nation=self.nation_lvl,
                color='totw_silver'
            )

            self.player_totw_bronze = Player.objects.create(
                ea_id=3,
                first_name='John',
                last_name='Doe',
                common_name='John Doe TOTW Bronze',
                nation=self.nation_lvl,
                color='totw_bronze'
            )

            self.player_rare_gold = Player.objects.create(
                ea_id=4,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Rare Gold',
                nation=self.nation_lvl,
                color='rare_gold'
            )

            self.player_rare_silver = Player.objects.create(
                ea_id=5,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Rare Silver',
                nation=self.nation_lvl,
                color='rare_silver'
            )

            self.player_rare_bronze = Player.objects.create(
                ea_id=6,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Rare Bronze',
                nation=self.nation_lvl,
                color='rare_bronze'
            )

            self.player_gold = Player.objects.create(
                ea_id=7,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Gold',
                nation=self.nation_lvl,
                color='gold'
            )

            self.player_silver = Player.objects.create(
                ea_id=8,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Silver',
                nation=self.nation_lvl,
                color='silver'
            )

            self.player_bronze = Player.objects.create(
                ea_id=9,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Bronze',
                nation=self.nation_lvl,
                color='bronze'
            )

            self.player_legend = Player.objects.create(
                ea_id=10,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Legend',
                nation=self.nation_lvl,
                color='legend'
            )

    def test_ea_detail_view_player_pagination(self):
        # Player pagination
        view = default_nation_detail_view(self, self.nation_pos)
        data = view.get_context_data()

        self.assertEqual(data['players'].paginator.num_pages, 1)

        data['players'] = view.pagination(Player.objects.all(), 1)

        self.assertEqual(data['players'].paginator.num_pages, 27)

    def test_ea_detail_view_filter_position(self):  # pylint: disable=too-many-locals, too-many-statements
        # Player filter by position
        view_all = default_nation_detail_view(self, self.nation_pos, data={'pos': 'all'})
        view_def = default_nation_detail_view(self, self.nation_pos, data={'pos': 'def'})
        view_mid = default_nation_detail_view(self, self.nation_pos, data={'pos': 'mid'})
        view_att = default_nation_detail_view(self, self.nation_pos, data={'pos': 'att'})
        view_rbs = default_nation_detail_view(self, self.nation_pos, data={'pos': 'rbs'})
        view_lbs = default_nation_detail_view(self, self.nation_pos, data={'pos': 'lbs'})
        view_rms = default_nation_detail_view(self, self.nation_pos, data={'pos': 'rms'})
        view_lms = default_nation_detail_view(self, self.nation_pos, data={'pos': 'lms'})
        view_cms = default_nation_detail_view(self, self.nation_pos, data={'pos': 'cms'})
        view_sts = default_nation_detail_view(self, self.nation_pos, data={'pos': 'sts'})
        view_gk = default_nation_detail_view(self, self.nation_pos, data={'pos': 'gk'})
        view_rwb = default_nation_detail_view(self, self.nation_pos, data={'pos': 'rwb'})
        view_rb = default_nation_detail_view(self, self.nation_pos, data={'pos': 'rb'})
        view_cb = default_nation_detail_view(self, self.nation_pos, data={'pos': 'cb'})
        view_lb = default_nation_detail_view(self, self.nation_pos, data={'pos': 'lb'})
        view_lwb = default_nation_detail_view(self, self.nation_pos, data={'pos': 'lwb'})
        view_cdm = default_nation_detail_view(self, self.nation_pos, data={'pos': 'cdm'})
        view_cm = default_nation_detail_view(self, self.nation_pos, data={'pos': 'cm'})
        view_cam = default_nation_detail_view(self, self.nation_pos, data={'pos': 'cam'})
        view_rm = default_nation_detail_view(self, self.nation_pos, data={'pos': 'rm'})
        view_rw = default_nation_detail_view(self, self.nation_pos, data={'pos': 'rw'})
        view_rf = default_nation_detail_view(self, self.nation_pos, data={'pos': 'rf'})
        view_lm = default_nation_detail_view(self, self.nation_pos, data={'pos': 'lm'})
        view_lw = default_nation_detail_view(self, self.nation_pos, data={'pos': 'lw'})
        view_lf = default_nation_detail_view(self, self.nation_pos, data={'pos': 'lf'})
        view_cf = default_nation_detail_view(self, self.nation_pos, data={'pos': 'cf'})
        view_st = default_nation_detail_view(self, self.nation_pos, data={'pos': 'st'})

        data_all = view_all.get_context_data()
        data_def = view_def.get_context_data()
        data_mid = view_mid.get_context_data()
        data_att = view_att.get_context_data()
        data_rbs = view_rbs.get_context_data()
        data_lbs = view_lbs.get_context_data()
        data_rms = view_rms.get_context_data()
        data_lms = view_lms.get_context_data()
        data_cms = view_cms.get_context_data()
        data_sts = view_sts.get_context_data()
        data_gk = view_gk.get_context_data()
        data_rwb = view_rwb.get_context_data()
        data_rb = view_rb.get_context_data()
        data_cb = view_cb.get_context_data()
        data_lb = view_lb.get_context_data()
        data_lwb = view_lwb.get_context_data()
        data_cdm = view_cdm.get_context_data()
        data_cm = view_cm.get_context_data()
        data_cam = view_cam.get_context_data()
        data_rm = view_rm.get_context_data()
        data_rw = view_rw.get_context_data()
        data_rf = view_rf.get_context_data()
        data_lm = view_lm.get_context_data()
        data_lw = view_lw.get_context_data()
        data_lf = view_lf.get_context_data()
        data_cf = view_cf.get_context_data()
        data_st = view_st.get_context_data()

        self.assertEqual(list(data_all['players'].object_list), [self.player_st, self.player_cf,
                                                                 self.player_lf, self.player_lw, self.player_lm,
                                                                 self.player_rf, self.player_rw, self.player_rm,
                                                                 self.player_cam, self.player_cm, self.player_cdm,
                                                                 self.player_lwb, self.player_lb,
                                                                 self.player_cb,
                                                                 self.player_rb, self.player_rwb,
                                                                 self.player_gk])
        self.assertEqual(list(data_def['players'].object_list), [self.player_lwb, self.player_lb,
                                                                 self.player_cb,
                                                                 self.player_rb, self.player_rwb])
        self.assertEqual(list(data_mid['players'].object_list), [self.player_lf, self.player_lw, self.player_lm,
                                                                 self.player_rf, self.player_rw, self.player_rm,
                                                                 self.player_cam, self.player_cm, self.player_cdm])
        self.assertEqual(list(data_att['players'].object_list), [self.player_st, self.player_cf])
        self.assertEqual(list(data_rbs['players'].object_list), [self.player_rb, self.player_rwb])
        self.assertEqual(list(data_lbs['players'].object_list), [self.player_lwb, self.player_lb])
        self.assertEqual(list(data_rms['players'].object_list), [self.player_rf, self.player_rw, self.player_rm])
        self.assertEqual(list(data_lms['players'].object_list), [self.player_lf, self.player_lw, self.player_lm])
        self.assertEqual(list(data_cms['players'].object_list), [self.player_cam, self.player_cm, self.player_cdm])
        self.assertEqual(list(data_sts['players'].object_list), [self.player_st, self.player_cf])
        self.assertEqual(list(data_gk['players'].object_list), [self.player_gk])
        self.assertEqual(list(data_rwb['players'].object_list), [self.player_rwb])
        self.assertEqual(list(data_rb['players'].object_list), [self.player_rb])
        self.assertEqual(list(data_cb['players'].object_list), [self.player_cb])
        self.assertEqual(list(data_lb['players'].object_list), [self.player_lb])
        self.assertEqual(list(data_lwb['players'].object_list), [self.player_lwb])
        self.assertEqual(list(data_cdm['players'].object_list), [self.player_cdm])
        self.assertEqual(list(data_cm['players'].object_list), [self.player_cm])
        self.assertEqual(list(data_cam['players'].object_list), [self.player_cam])
        self.assertEqual(list(data_rm['players'].object_list), [self.player_rm])
        self.assertEqual(list(data_rw['players'].object_list), [self.player_rw])
        self.assertEqual(list(data_rf['players'].object_list), [self.player_rf])
        self.assertEqual(list(data_lm['players'].object_list), [self.player_lm])
        self.assertEqual(list(data_lw['players'].object_list), [self.player_lw])
        self.assertEqual(list(data_lf['players'].object_list), [self.player_lf])
        self.assertEqual(list(data_cf['players'].object_list), [self.player_cf])
        self.assertEqual(list(data_st['players'].object_list), [self.player_st])

    def test_ea_detail_view_filter_level(self):  # pylint: disable=too-many-locals, too-many-statements
        view_all = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'all'})
        view_gold = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'gold'})
        view_silver = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'silver'})
        view_bronze = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'bronze'})
        view_totw_all = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'totw_all'})
        view_totw_gold = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'totw_gold'})
        view_totw_silver = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'totw_silver'})
        view_totw_bronze = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'totw_bronze'})
        view_rare_all = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'rare_all'})
        view_rare_gold = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'rare_gold'})
        view_rare_silver = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'rare_silver'})
        view_rare_bronze = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'rare_bronze'})
        view_nonrare_all = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'nonrare_all'})
        view_nonrare_gold = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'nonrare_gold'})
        view_nonrare_silver = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'nonrare_silver'})
        view_nonrare_bronze = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'nonrare_bronze'})
        view_legends = default_nation_detail_view(self, self.nation_lvl, data={'lvl': 'legend'})

        data_all = view_all.get_context_data()
        data_gold = view_gold.get_context_data()
        data_silver = view_silver.get_context_data()
        data_bronze = view_bronze.get_context_data()
        data_totw_all = view_totw_all.get_context_data()
        data_totw_gold = view_totw_gold.get_context_data()
        data_totw_silver = view_totw_silver.get_context_data()
        data_totw_bronze = view_totw_bronze.get_context_data()
        data_rare_all = view_rare_all.get_context_data()
        data_rare_gold = view_rare_gold.get_context_data()
        data_rare_silver = view_rare_silver.get_context_data()
        data_rare_bronze = view_rare_bronze.get_context_data()
        data_nonrare_all = view_nonrare_all.get_context_data()
        data_nonrare_gold = view_nonrare_gold.get_context_data()
        data_nonrare_silver = view_nonrare_silver.get_context_data()
        data_nonrare_bronze = view_nonrare_bronze.get_context_data()
        data_legends = view_legends.get_context_data()

        self.assertEqual(list(data_all['players'].object_list), [self.player_legend, self.player_bronze,
                                                                 self.player_silver, self.player_gold,
                                                                 self.player_rare_bronze, self.player_rare_silver,
                                                                 self.player_rare_gold, self.player_totw_bronze,
                                                                 self.player_totw_silver, self.player_totw_gold])
        self.assertEqual(list(data_gold['players'].object_list), [self.player_gold, self.player_rare_gold,
                                                                  self.player_totw_gold])
        self.assertEqual(list(data_silver['players'].object_list), [self.player_silver, self.player_rare_silver,
                                                                    self.player_totw_silver])
        self.assertEqual(list(data_bronze['players'].object_list), [self.player_bronze, self.player_rare_bronze,
                                                                    self.player_totw_bronze])
        self.assertEqual(list(data_totw_all['players'].object_list), [self.player_totw_bronze, self.player_totw_silver,
                                                                      self.player_totw_gold])
        self.assertEqual(list(data_totw_gold['players'].object_list), [self.player_totw_gold])
        self.assertEqual(list(data_totw_silver['players'].object_list), [self.player_totw_silver])
        self.assertEqual(list(data_totw_bronze['players'].object_list), [self.player_totw_bronze])
        self.assertEqual(list(data_rare_all['players'].object_list), [self.player_rare_bronze, self.player_rare_silver,
                                                                      self.player_rare_gold])
        self.assertEqual(list(data_rare_gold['players'].object_list), [self.player_rare_gold])
        self.assertEqual(list(data_rare_silver['players'].object_list), [self.player_rare_silver])
        self.assertEqual(list(data_rare_bronze['players'].object_list), [self.player_rare_bronze])
        self.assertEqual(list(data_nonrare_all['players'].object_list), [self.player_bronze, self.player_silver,
                                                                         self.player_gold])
        self.assertEqual(list(data_nonrare_gold['players'].object_list), [self.player_gold])
        self.assertEqual(list(data_nonrare_silver['players'].object_list), [self.player_silver])
        self.assertEqual(list(data_nonrare_bronze['players'].object_list), [self.player_bronze])
        self.assertEqual(list(data_legends['players'].object_list), [self.player_legend])

    def test_ea_detail_view_sort_by(self):
        view_rating = default_nation_detail_view(self, self.nation_pos, data={'sort': 'rating'})
        view_pace = default_nation_detail_view(self, self.nation_pos, data={'sort': 'pace'})
        view_shooting = default_nation_detail_view(self, self.nation_pos, data={'sort': 'shooting'})
        view_passing = default_nation_detail_view(self, self.nation_pos, data={'sort': 'passing'})
        view_dribbling = default_nation_detail_view(self, self.nation_pos, data={'sort': 'dribbling'})
        view_defending = default_nation_detail_view(self, self.nation_pos, data={'sort': 'defending'})
        view_physical = default_nation_detail_view(self, self.nation_pos, data={'sort': 'physical'})

        data_rating = view_rating.get_context_data()
        data_pace = view_pace.get_context_data()
        data_shooting = view_shooting.get_context_data()
        data_passing = view_passing.get_context_data()
        data_dribbling = view_dribbling.get_context_data()
        data_defending = view_defending.get_context_data()
        data_physical = view_physical.get_context_data()

        self.assertEqual(list(data_rating['players'].object_list), [self.player_st, self.player_cf,
                                                                    self.player_lf, self.player_lw, self.player_lm,
                                                                    self.player_rf, self.player_rw, self.player_rm,
                                                                    self.player_cam, self.player_cm, self.player_cdm,
                                                                    self.player_lwb, self.player_lb,
                                                                    self.player_cb,
                                                                    self.player_rb, self.player_rwb,
                                                                    self.player_gk])
        self.assertEqual(list(data_pace['players'].object_list), [self.player_st, self.player_cf,
                                                                  self.player_lf, self.player_lw, self.player_lm,
                                                                  self.player_rf, self.player_rw, self.player_rm,
                                                                  self.player_cam, self.player_cm, self.player_cdm,
                                                                  self.player_lwb, self.player_lb,
                                                                  self.player_cb,
                                                                  self.player_rb, self.player_rwb,
                                                                  self.player_gk])
        self.assertEqual(list(data_shooting['players'].object_list), [self.player_gk,
                                                                      self.player_rwb, self.player_rb,
                                                                      self.player_cb,
                                                                      self.player_lb, self.player_lwb,
                                                                      self.player_cdm, self.player_cm, self.player_cam,
                                                                      self.player_rm, self.player_rw, self.player_rf,
                                                                      self.player_lm, self.player_lw, self.player_lf,
                                                                      self.player_cf, self.player_st])
        self.assertEqual(list(data_passing['players'].object_list), [self.player_st, self.player_cf,
                                                                     self.player_lf, self.player_lw, self.player_lm,
                                                                     self.player_rf, self.player_rw, self.player_rm,
                                                                     self.player_cam, self.player_cm, self.player_cdm,
                                                                     self.player_lwb, self.player_lb,
                                                                     self.player_cb,
                                                                     self.player_rb, self.player_rwb,
                                                                     self.player_gk])
        self.assertEqual(list(data_dribbling['players'].object_list), [self.player_gk,
                                                                       self.player_rwb, self.player_rb,
                                                                       self.player_cb,
                                                                       self.player_lb, self.player_lwb,
                                                                       self.player_cdm, self.player_cm, self.player_cam,
                                                                       self.player_rm, self.player_rw, self.player_rf,
                                                                       self.player_lm, self.player_lw, self.player_lf,
                                                                       self.player_cf, self.player_st])
        self.assertEqual(list(data_defending['players'].object_list), [self.player_st, self.player_cf,
                                                                       self.player_lf, self.player_lw, self.player_lm,
                                                                       self.player_rf, self.player_rw, self.player_rm,
                                                                       self.player_cam, self.player_cm, self.player_cdm,
                                                                       self.player_lwb, self.player_lb,
                                                                       self.player_cb,
                                                                       self.player_rb, self.player_rwb,
                                                                       self.player_gk])
        self.assertEqual(list(data_physical['players'].object_list), [self.player_gk,
                                                                      self.player_rwb, self.player_rb,
                                                                      self.player_cb,
                                                                      self.player_lb, self.player_lwb,
                                                                      self.player_cdm, self.player_cm, self.player_cam,
                                                                      self.player_rm, self.player_rw, self.player_rf,
                                                                      self.player_lm, self.player_lw, self.player_lf,
                                                                      self.player_cf, self.player_st])


class TestLeagueDetailView(EaDetailView):
    model = League


class TestLeagueEaDetailView(TestCase):  # pylint: disable=too-many-instance-attributes
    def setUp(self):
        self.factory = RequestFactory()

        with externals.watson.context_manager('update_index')():
            content_type = ContentType.objects.get_for_model(Leagues)

            self.page = Page.objects.create(
                title='Leagues',
                slug='leagues',
                content_type=content_type
            )

            self.leagues = Leagues.objects.create(
                page=self.page
            )

            self.league_pos = League.objects.create(
                page=self.leagues,
                ea_id=1,
                name='League pos',
                name_abbr='League pos',
                slug='league_pos',
                average_rating=10.0,
                total_players=10,
                total_bronze=10,
                total_silver=10,
                total_gold=10,
                total_inform=10,
                total_special=10
            )

            self.league_lvl = League.objects.create(
                page=self.leagues,
                ea_id=2,
                name='League lvl',
                name_abbr='League lvl',
                slug='league_lvl',
                average_rating=10.0,
                total_players=10,
                total_bronze=10,
                total_silver=10,
                total_gold=10,
                total_inform=10,
                total_special=10
            )

            self.player_gk = Player.objects.create(
                ea_id=1,
                first_name='John',
                last_name='Doe',
                common_name='John Doe GK',
                league=self.league_pos,
                position='GK',
                rating=1,
                card_att_1=1,
                card_att_2=17,
                card_att_3=1,
                card_att_4=17,
                card_att_5=1,
                card_att_6=17
            )

            self.player_rwb = Player.objects.create(
                ea_id=2,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RWB',
                league=self.league_pos,
                position='RWB',
                rating=2,
                card_att_1=2,
                card_att_2=16,
                card_att_3=2,
                card_att_4=16,
                card_att_5=2,
                card_att_6=16
            )

            self.player_rb = Player.objects.create(
                ea_id=3,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RB',
                league=self.league_pos,
                position='RB',
                rating=3,
                card_att_1=3,
                card_att_2=15,
                card_att_3=3,
                card_att_4=15,
                card_att_5=3,
                card_att_6=15
            )

            self.player_cb = Player.objects.create(
                ea_id=4,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CB',
                league=self.league_pos,
                position='CB',
                rating=4,
                card_att_1=4,
                card_att_2=14,
                card_att_3=4,
                card_att_4=14,
                card_att_5=4,
                card_att_6=14
            )

            self.player_lb = Player.objects.create(
                ea_id=5,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LB',
                league=self.league_pos,
                position='LB',
                rating=5,
                card_att_1=5,
                card_att_2=13,
                card_att_3=5,
                card_att_4=13,
                card_att_5=5,
                card_att_6=13
            )

            self.player_lwb = Player.objects.create(
                ea_id=6,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LWB',
                league=self.league_pos,
                position='LWB',
                rating=6,
                card_att_1=6,
                card_att_2=12,
                card_att_3=6,
                card_att_4=12,
                card_att_5=6,
                card_att_6=12
            )

            self.player_cdm = Player.objects.create(
                ea_id=7,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CDM',
                league=self.league_pos,
                position='CDM',
                rating=7,
                card_att_1=7,
                card_att_2=11,
                card_att_3=7,
                card_att_4=11,
                card_att_5=7,
                card_att_6=11
            )

            self.player_cm = Player.objects.create(
                ea_id=8,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CM',
                league=self.league_pos,
                position='CM',
                rating=8,
                card_att_1=8,
                card_att_2=10,
                card_att_3=8,
                card_att_4=10,
                card_att_5=8,
                card_att_6=10
            )

            self.player_cam = Player.objects.create(
                ea_id=9,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CAM',
                league=self.league_pos,
                position='CAM',
                rating=9,
                card_att_1=9,
                card_att_2=9,
                card_att_3=9,
                card_att_4=9,
                card_att_5=9,
                card_att_6=9
            )

            self.player_rm = Player.objects.create(
                ea_id=10,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RM',
                league=self.league_pos,
                position='RM',
                rating=10,
                card_att_1=10,
                card_att_2=8,
                card_att_3=10,
                card_att_4=8,
                card_att_5=10,
                card_att_6=8
            )

            self.player_rw = Player.objects.create(
                ea_id=11,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RW',
                league=self.league_pos,
                position='RW',
                rating=11,
                card_att_1=11,
                card_att_2=7,
                card_att_3=11,
                card_att_4=7,
                card_att_5=11,
                card_att_6=7
            )

            self.player_rf = Player.objects.create(
                ea_id=12,
                first_name='John',
                last_name='Doe',
                common_name='John Doe RF',
                league=self.league_pos,
                position='RF',
                rating=12,
                card_att_1=12,
                card_att_2=6,
                card_att_3=12,
                card_att_4=6,
                card_att_5=12,
                card_att_6=6
            )

            self.player_lm = Player.objects.create(
                ea_id=13,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LM',
                league=self.league_pos,
                position='LM',
                rating=13,
                card_att_1=13,
                card_att_2=5,
                card_att_3=13,
                card_att_4=5,
                card_att_5=13,
                card_att_6=5
            )

            self.player_lw = Player.objects.create(
                ea_id=14,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LW',
                league=self.league_pos,
                position='LW',
                rating=14,
                card_att_1=14,
                card_att_2=4,
                card_att_3=14,
                card_att_4=4,
                card_att_5=14,
                card_att_6=4
            )

            self.player_lf = Player.objects.create(
                ea_id=15,
                first_name='John',
                last_name='Doe',
                common_name='John Doe LF',
                league=self.league_pos,
                position='LF',
                rating=15,
                card_att_1=15,
                card_att_2=3,
                card_att_3=15,
                card_att_4=3,
                card_att_5=15,
                card_att_6=3
            )

            self.player_cf = Player.objects.create(
                ea_id=16,
                first_name='John',
                last_name='Doe',
                common_name='John Doe CF',
                league=self.league_pos,
                position='CF',
                rating=16,
                card_att_1=16,
                card_att_2=2,
                card_att_3=16,
                card_att_4=2,
                card_att_5=16,
                card_att_6=2
            )

            self.player_st = Player.objects.create(
                ea_id=17,
                first_name='John',
                last_name='Doe',
                common_name='John Doe ST',
                league=self.league_pos,
                position='ST',
                rating=17,
                card_att_1=17,
                card_att_2=1,
                card_att_3=17,
                card_att_4=1,
                card_att_5=17,
                card_att_6=1
            )

            self.player_totw_gold = Player.objects.create(
                ea_id=1,
                first_name='John',
                last_name='Doe',
                common_name='John Doe TOTW Gold',
                league=self.league_lvl,
                color='totw_gold'
            )

            self.player_totw_silver = Player.objects.create(
                ea_id=2,
                first_name='John',
                last_name='Doe',
                common_name='John Doe TOTW Silver',
                league=self.league_lvl,
                color='totw_silver'
            )

            self.player_totw_bronze = Player.objects.create(
                ea_id=3,
                first_name='John',
                last_name='Doe',
                common_name='John Doe TOTW Bronze',
                league=self.league_lvl,
                color='totw_bronze'
            )

            self.player_rare_gold = Player.objects.create(
                ea_id=4,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Rare Gold',
                league=self.league_lvl,
                color='rare_gold'
            )

            self.player_rare_silver = Player.objects.create(
                ea_id=5,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Rare Silver',
                league=self.league_lvl,
                color='rare_silver'
            )

            self.player_rare_bronze = Player.objects.create(
                ea_id=6,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Rare Bronze',
                league=self.league_lvl,
                color='rare_bronze'
            )

            self.player_gold = Player.objects.create(
                ea_id=7,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Gold',
                league=self.league_lvl,
                color='gold'
            )

            self.player_silver = Player.objects.create(
                ea_id=8,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Silver',
                league=self.league_lvl,
                color='silver'
            )

            self.player_bronze = Player.objects.create(
                ea_id=9,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Bronze',
                league=self.league_lvl,
                color='bronze'
            )

            self.player_legend = Player.objects.create(
                ea_id=10,
                first_name='John',
                last_name='Doe',
                common_name='John Doe Legend',
                league=self.league_lvl,
                color='legend'
            )

    def test_ea_detail_view_player_pagination(self):
        # Player pagination
        view = default_league_detail_view(self, self.league_pos)
        data = view.get_context_data()

        self.assertEqual(data['players'].paginator.num_pages, 1)

        data['players'] = view.pagination(Player.objects.all(), 1)

        self.assertEqual(data['players'].paginator.num_pages, 27)

    def test_ea_detail_view_filter_position(self):  # pylint: disable=too-many-locals, too-many-statements
        # Player filter by position
        view_all = default_league_detail_view(self, self.league_pos, data={'pos': 'all'})
        view_def = default_league_detail_view(self, self.league_pos, data={'pos': 'def'})
        view_mid = default_league_detail_view(self, self.league_pos, data={'pos': 'mid'})
        view_att = default_league_detail_view(self, self.league_pos, data={'pos': 'att'})
        view_rbs = default_league_detail_view(self, self.league_pos, data={'pos': 'rbs'})
        view_lbs = default_league_detail_view(self, self.league_pos, data={'pos': 'lbs'})
        view_rms = default_league_detail_view(self, self.league_pos, data={'pos': 'rms'})
        view_lms = default_league_detail_view(self, self.league_pos, data={'pos': 'lms'})
        view_cms = default_league_detail_view(self, self.league_pos, data={'pos': 'cms'})
        view_sts = default_league_detail_view(self, self.league_pos, data={'pos': 'sts'})
        view_gk = default_league_detail_view(self, self.league_pos, data={'pos': 'gk'})
        view_rwb = default_league_detail_view(self, self.league_pos, data={'pos': 'rwb'})
        view_rb = default_league_detail_view(self, self.league_pos, data={'pos': 'rb'})
        view_cb = default_league_detail_view(self, self.league_pos, data={'pos': 'cb'})
        view_lb = default_league_detail_view(self, self.league_pos, data={'pos': 'lb'})
        view_lwb = default_league_detail_view(self, self.league_pos, data={'pos': 'lwb'})
        view_cdm = default_league_detail_view(self, self.league_pos, data={'pos': 'cdm'})
        view_cm = default_league_detail_view(self, self.league_pos, data={'pos': 'cm'})
        view_cam = default_league_detail_view(self, self.league_pos, data={'pos': 'cam'})
        view_rm = default_league_detail_view(self, self.league_pos, data={'pos': 'rm'})
        view_rw = default_league_detail_view(self, self.league_pos, data={'pos': 'rw'})
        view_rf = default_league_detail_view(self, self.league_pos, data={'pos': 'rf'})
        view_lm = default_league_detail_view(self, self.league_pos, data={'pos': 'lm'})
        view_lw = default_league_detail_view(self, self.league_pos, data={'pos': 'lw'})
        view_lf = default_league_detail_view(self, self.league_pos, data={'pos': 'lf'})
        view_cf = default_league_detail_view(self, self.league_pos, data={'pos': 'cf'})
        view_st = default_league_detail_view(self, self.league_pos, data={'pos': 'st'})

        data_all = view_all.get_context_data()
        data_def = view_def.get_context_data()
        data_mid = view_mid.get_context_data()
        data_att = view_att.get_context_data()
        data_rbs = view_rbs.get_context_data()
        data_lbs = view_lbs.get_context_data()
        data_rms = view_rms.get_context_data()
        data_lms = view_lms.get_context_data()
        data_cms = view_cms.get_context_data()
        data_sts = view_sts.get_context_data()
        data_gk = view_gk.get_context_data()
        data_rwb = view_rwb.get_context_data()
        data_rb = view_rb.get_context_data()
        data_cb = view_cb.get_context_data()
        data_lb = view_lb.get_context_data()
        data_lwb = view_lwb.get_context_data()
        data_cdm = view_cdm.get_context_data()
        data_cm = view_cm.get_context_data()
        data_cam = view_cam.get_context_data()
        data_rm = view_rm.get_context_data()
        data_rw = view_rw.get_context_data()
        data_rf = view_rf.get_context_data()
        data_lm = view_lm.get_context_data()
        data_lw = view_lw.get_context_data()
        data_lf = view_lf.get_context_data()
        data_cf = view_cf.get_context_data()
        data_st = view_st.get_context_data()

        self.assertEqual(list(data_all['players'].object_list), [self.player_st, self.player_cf,
                                                                 self.player_lf, self.player_lw, self.player_lm,
                                                                 self.player_rf, self.player_rw, self.player_rm,
                                                                 self.player_cam, self.player_cm, self.player_cdm,
                                                                 self.player_lwb, self.player_lb,
                                                                 self.player_cb,
                                                                 self.player_rb, self.player_rwb,
                                                                 self.player_gk])
        self.assertEqual(list(data_def['players'].object_list), [self.player_lwb, self.player_lb,
                                                                 self.player_cb,
                                                                 self.player_rb, self.player_rwb])
        self.assertEqual(list(data_mid['players'].object_list), [self.player_lf, self.player_lw, self.player_lm,
                                                                 self.player_rf, self.player_rw, self.player_rm,
                                                                 self.player_cam, self.player_cm, self.player_cdm])
        self.assertEqual(list(data_att['players'].object_list), [self.player_st, self.player_cf])
        self.assertEqual(list(data_rbs['players'].object_list), [self.player_rb, self.player_rwb])
        self.assertEqual(list(data_lbs['players'].object_list), [self.player_lwb, self.player_lb])
        self.assertEqual(list(data_rms['players'].object_list), [self.player_rf, self.player_rw, self.player_rm])
        self.assertEqual(list(data_lms['players'].object_list), [self.player_lf, self.player_lw, self.player_lm])
        self.assertEqual(list(data_cms['players'].object_list), [self.player_cam, self.player_cm, self.player_cdm])
        self.assertEqual(list(data_sts['players'].object_list), [self.player_st, self.player_cf])
        self.assertEqual(list(data_gk['players'].object_list), [self.player_gk])
        self.assertEqual(list(data_rwb['players'].object_list), [self.player_rwb])
        self.assertEqual(list(data_rb['players'].object_list), [self.player_rb])
        self.assertEqual(list(data_cb['players'].object_list), [self.player_cb])
        self.assertEqual(list(data_lb['players'].object_list), [self.player_lb])
        self.assertEqual(list(data_lwb['players'].object_list), [self.player_lwb])
        self.assertEqual(list(data_cdm['players'].object_list), [self.player_cdm])
        self.assertEqual(list(data_cm['players'].object_list), [self.player_cm])
        self.assertEqual(list(data_cam['players'].object_list), [self.player_cam])
        self.assertEqual(list(data_rm['players'].object_list), [self.player_rm])
        self.assertEqual(list(data_rw['players'].object_list), [self.player_rw])
        self.assertEqual(list(data_rf['players'].object_list), [self.player_rf])
        self.assertEqual(list(data_lm['players'].object_list), [self.player_lm])
        self.assertEqual(list(data_lw['players'].object_list), [self.player_lw])
        self.assertEqual(list(data_lf['players'].object_list), [self.player_lf])
        self.assertEqual(list(data_cf['players'].object_list), [self.player_cf])
        self.assertEqual(list(data_st['players'].object_list), [self.player_st])

    def test_ea_detail_view_filter_level(self):  # pylint: disable=too-many-locals, too-many-statements
        view_all = default_league_detail_view(self, self.league_lvl, data={'lvl': 'all'})
        view_gold = default_league_detail_view(self, self.league_lvl, data={'lvl': 'gold'})
        view_silver = default_league_detail_view(self, self.league_lvl, data={'lvl': 'silver'})
        view_bronze = default_league_detail_view(self, self.league_lvl, data={'lvl': 'bronze'})
        view_totw_all = default_league_detail_view(self, self.league_lvl, data={'lvl': 'totw_all'})
        view_totw_gold = default_league_detail_view(self, self.league_lvl, data={'lvl': 'totw_gold'})
        view_totw_silver = default_league_detail_view(self, self.league_lvl, data={'lvl': 'totw_silver'})
        view_totw_bronze = default_league_detail_view(self, self.league_lvl, data={'lvl': 'totw_bronze'})
        view_rare_all = default_league_detail_view(self, self.league_lvl, data={'lvl': 'rare_all'})
        view_rare_gold = default_league_detail_view(self, self.league_lvl, data={'lvl': 'rare_gold'})
        view_rare_silver = default_league_detail_view(self, self.league_lvl, data={'lvl': 'rare_silver'})
        view_rare_bronze = default_league_detail_view(self, self.league_lvl, data={'lvl': 'rare_bronze'})
        view_nonrare_all = default_league_detail_view(self, self.league_lvl, data={'lvl': 'nonrare_all'})
        view_nonrare_gold = default_league_detail_view(self, self.league_lvl, data={'lvl': 'nonrare_gold'})
        view_nonrare_silver = default_league_detail_view(self, self.league_lvl, data={'lvl': 'nonrare_silver'})
        view_nonrare_bronze = default_league_detail_view(self, self.league_lvl, data={'lvl': 'nonrare_bronze'})
        view_legends = default_league_detail_view(self, self.league_lvl, data={'lvl': 'legend'})

        data_all = view_all.get_context_data()
        data_gold = view_gold.get_context_data()
        data_silver = view_silver.get_context_data()
        data_bronze = view_bronze.get_context_data()
        data_totw_all = view_totw_all.get_context_data()
        data_totw_gold = view_totw_gold.get_context_data()
        data_totw_silver = view_totw_silver.get_context_data()
        data_totw_bronze = view_totw_bronze.get_context_data()
        data_rare_all = view_rare_all.get_context_data()
        data_rare_gold = view_rare_gold.get_context_data()
        data_rare_silver = view_rare_silver.get_context_data()
        data_rare_bronze = view_rare_bronze.get_context_data()
        data_nonrare_all = view_nonrare_all.get_context_data()
        data_nonrare_gold = view_nonrare_gold.get_context_data()
        data_nonrare_silver = view_nonrare_silver.get_context_data()
        data_nonrare_bronze = view_nonrare_bronze.get_context_data()
        data_legends = view_legends.get_context_data()

        self.assertEqual(list(data_all['players'].object_list), [self.player_legend, self.player_bronze,
                                                                 self.player_silver, self.player_gold,
                                                                 self.player_rare_bronze, self.player_rare_silver,
                                                                 self.player_rare_gold, self.player_totw_bronze,
                                                                 self.player_totw_silver, self.player_totw_gold])
        self.assertEqual(list(data_gold['players'].object_list), [self.player_gold, self.player_rare_gold,
                                                                  self.player_totw_gold])
        self.assertEqual(list(data_silver['players'].object_list), [self.player_silver, self.player_rare_silver,
                                                                    self.player_totw_silver])
        self.assertEqual(list(data_bronze['players'].object_list), [self.player_bronze, self.player_rare_bronze,
                                                                    self.player_totw_bronze])
        self.assertEqual(list(data_totw_all['players'].object_list), [self.player_totw_bronze, self.player_totw_silver,
                                                                      self.player_totw_gold])
        self.assertEqual(list(data_totw_gold['players'].object_list), [self.player_totw_gold])
        self.assertEqual(list(data_totw_silver['players'].object_list), [self.player_totw_silver])
        self.assertEqual(list(data_totw_bronze['players'].object_list), [self.player_totw_bronze])
        self.assertEqual(list(data_rare_all['players'].object_list), [self.player_rare_bronze, self.player_rare_silver,
                                                                      self.player_rare_gold])
        self.assertEqual(list(data_rare_gold['players'].object_list), [self.player_rare_gold])
        self.assertEqual(list(data_rare_silver['players'].object_list), [self.player_rare_silver])
        self.assertEqual(list(data_rare_bronze['players'].object_list), [self.player_rare_bronze])
        self.assertEqual(list(data_nonrare_all['players'].object_list), [self.player_bronze, self.player_silver,
                                                                         self.player_gold])
        self.assertEqual(list(data_nonrare_gold['players'].object_list), [self.player_gold])
        self.assertEqual(list(data_nonrare_silver['players'].object_list), [self.player_silver])
        self.assertEqual(list(data_nonrare_bronze['players'].object_list), [self.player_bronze])
        self.assertEqual(list(data_legends['players'].object_list), [self.player_legend])

    def test_ea_detail_view_sort_by(self):
        view_rating = default_league_detail_view(self, self.league_pos, data={'sort': 'rating'})
        view_pace = default_league_detail_view(self, self.league_pos, data={'sort': 'pace'})
        view_shooting = default_league_detail_view(self, self.league_pos, data={'sort': 'shooting'})
        view_passing = default_league_detail_view(self, self.league_pos, data={'sort': 'passing'})
        view_dribbling = default_league_detail_view(self, self.league_pos, data={'sort': 'dribbling'})
        view_defending = default_league_detail_view(self, self.league_pos, data={'sort': 'defending'})
        view_physical = default_league_detail_view(self, self.league_pos, data={'sort': 'physical'})

        data_rating = view_rating.get_context_data()
        data_pace = view_pace.get_context_data()
        data_shooting = view_shooting.get_context_data()
        data_passing = view_passing.get_context_data()
        data_dribbling = view_dribbling.get_context_data()
        data_defending = view_defending.get_context_data()
        data_physical = view_physical.get_context_data()

        self.assertEqual(list(data_rating['players'].object_list), [self.player_st, self.player_cf,
                                                                    self.player_lf, self.player_lw, self.player_lm,
                                                                    self.player_rf, self.player_rw, self.player_rm,
                                                                    self.player_cam, self.player_cm, self.player_cdm,
                                                                    self.player_lwb, self.player_lb,
                                                                    self.player_cb,
                                                                    self.player_rb, self.player_rwb,
                                                                    self.player_gk])
        self.assertEqual(list(data_pace['players'].object_list), [self.player_st, self.player_cf,
                                                                  self.player_lf, self.player_lw, self.player_lm,
                                                                  self.player_rf, self.player_rw, self.player_rm,
                                                                  self.player_cam, self.player_cm, self.player_cdm,
                                                                  self.player_lwb, self.player_lb,
                                                                  self.player_cb,
                                                                  self.player_rb, self.player_rwb,
                                                                  self.player_gk])
        self.assertEqual(list(data_shooting['players'].object_list), [self.player_gk,
                                                                      self.player_rwb, self.player_rb,
                                                                      self.player_cb,
                                                                      self.player_lb, self.player_lwb,
                                                                      self.player_cdm, self.player_cm, self.player_cam,
                                                                      self.player_rm, self.player_rw, self.player_rf,
                                                                      self.player_lm, self.player_lw, self.player_lf,
                                                                      self.player_cf, self.player_st])
        self.assertEqual(list(data_passing['players'].object_list), [self.player_st, self.player_cf,
                                                                     self.player_lf, self.player_lw, self.player_lm,
                                                                     self.player_rf, self.player_rw, self.player_rm,
                                                                     self.player_cam, self.player_cm, self.player_cdm,
                                                                     self.player_lwb, self.player_lb,
                                                                     self.player_cb,
                                                                     self.player_rb, self.player_rwb,
                                                                     self.player_gk])
        self.assertEqual(list(data_dribbling['players'].object_list), [self.player_gk,
                                                                       self.player_rwb, self.player_rb,
                                                                       self.player_cb,
                                                                       self.player_lb, self.player_lwb,
                                                                       self.player_cdm, self.player_cm, self.player_cam,
                                                                       self.player_rm, self.player_rw, self.player_rf,
                                                                       self.player_lm, self.player_lw, self.player_lf,
                                                                       self.player_cf, self.player_st])
        self.assertEqual(list(data_defending['players'].object_list), [self.player_st, self.player_cf,
                                                                       self.player_lf, self.player_lw, self.player_lm,
                                                                       self.player_rf, self.player_rw, self.player_rm,
                                                                       self.player_cam, self.player_cm, self.player_cdm,
                                                                       self.player_lwb, self.player_lb,
                                                                       self.player_cb,
                                                                       self.player_rb, self.player_rwb,
                                                                       self.player_gk])
        self.assertEqual(list(data_physical['players'].object_list), [self.player_gk,
                                                                      self.player_rwb, self.player_rb,
                                                                      self.player_cb,
                                                                      self.player_lb, self.player_lwb,
                                                                      self.player_cdm, self.player_cm, self.player_cam,
                                                                      self.player_rm, self.player_rw, self.player_rf,
                                                                      self.player_lm, self.player_lw, self.player_lf,
                                                                      self.player_cf, self.player_st])


def default_nation_detail_view(obj, nation, url='/england/', data=None):  # pylint: disable=dangerous-default-value
    if data is None:
        data = {}

    view = TestNationDetailView()
    view.request = obj.factory.get(url, data=data)
    view.request.pages = RequestPageManager(view.request)
    view.object = nation
    view.kwargs = {'slug': nation.slug}

    return view


def default_league_detail_view(obj, league, url='/league-1/', data=None):  # pylint: disable=dangerous-default-value
    if data is None:
        data = {}

    view = TestLeagueDetailView()
    view.request = obj.factory.get(url, data=data)
    view.request.pages = RequestPageManager(view.request)
    view.object = league
    view.kwargs = {'slug': league.slug}

    return view
