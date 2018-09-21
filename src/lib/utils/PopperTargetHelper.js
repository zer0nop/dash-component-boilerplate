import PropTypes from 'prop-types';
import { getTarget, targetPropType } from '../../utils';
import { withPopperContext } from '../contexts/PopperContext'

const PopperTargetHelperBase = (props) => {
  props.context.popperManager.setTargetNode(getTarget(props.target));
  return null;
};

PopperTargetHelperBase.propTypes = {
  target: targetPropType.isRequired,
};

const PopperTargetHelper = withPopperContext(PopperTargetHelperBase)

export default PopperTargetHelper;
