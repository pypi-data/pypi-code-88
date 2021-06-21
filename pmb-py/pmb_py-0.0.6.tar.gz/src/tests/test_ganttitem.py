import pmb_py


def test_list_gantt_item(pmb):
    objs = pmb.api.GanttItems.list()
    assert objs


def test_create_gantt_item(pmb):
    obj = pmb.api.GanttItems.create(name='test1')
    assert type(obj) == pmb_py.domain.model.PmbGanttItem


def test_list_gantt_item_with_kwarg_name(pmb):
    objs = pmb.api.GanttItems.list(name='test1')
    for obj in objs:
        assert obj.name == 'test1'


def test_update_gantt_item(pmb):
    obj = pmb.api.GanttItems.get(name='test1')
    assert obj.name == 'test1'
    obj = pmb.api.GanttItems.update(obj.id, sg_task_id=100)
    assert obj.sg_task_id == 100
